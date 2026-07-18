import shutil
import os

import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma

from loaders import load_local_documents, load_websites

from config import (
    MISTRAL_API_KEY,
    CHROMA_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL
)


def build_database(urls=None):
    """
    Builds/Rebuilds the Chroma Vector Database.

    Parameters
    ----------
    urls : list
        Optional list of website URLs.
    """

    print("Loading local documents...")

    documents = load_local_documents()

    # Load websites if provided
    if urls:
        print("Loading websites...")
        documents.extend(load_websites(urls))
        print("\nLoaded documents:")
    for doc in documents:
        print(doc.metadata)

    if len(documents) == 0:
        print("No documents found.")
        return False

    print(f"Loaded {len(documents)} documents.")

    # -------------------------
    # Split Documents
    # -------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)
    print("\n===== CHUNKS =====")
    for i, chunk in enumerate(chunks[:5]):
        print(f"\nChunk {i+1}")
        print(chunk.metadata)
        print(chunk.page_content[:300])
        print(f"Generated {len(chunks)} chunks.")

    # -------------------------
    # Embeddings
    # -------------------------

    embedding_model = MistralAIEmbeddings(
        model=EMBEDDING_MODEL,
        api_key=MISTRAL_API_KEY
    )

    # -------------------------
    # Delete Old Database
    # -------------------------

    if os.path.exists(CHROMA_PATH):
      shutil.rmtree(CHROMA_PATH, ignore_errors=True)

    # Chroma caches a "system client" per persist_directory for the life of
    # the process. Since Streamlit keeps this process alive across reruns,
    # any earlier Chroma(...) call (e.g. from rag.py answering a question)
    # leaves a stale client pointing at the files we just deleted above.
    # Clear that cache so the next Chroma call opens a brand-new connection
    # instead of reusing the stale one - this is what causes the
    # "attempt to write a readonly database" error.
    chromadb.api.client.SharedSystemClient.clear_system_cache()

    # -------------------------
    # Create Database
    # -------------------------
    os.makedirs(CHROMA_PATH, exist_ok=True)
    Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    # Clear again so that after building, rag.py's get_retriever() also
    # opens a fresh client against the newly-built DB rather than any
    # cached reference from the build step itself.
    chromadb.api.client.SharedSystemClient.clear_system_cache()

    print("Database created successfully.")

    return True


# -------------------------
# Run directly
# -------------------------

if __name__ == "__main__":

    build_database()