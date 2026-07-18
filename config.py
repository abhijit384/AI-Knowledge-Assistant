import os
from dotenv import load_dotenv
import tempfile

load_dotenv()

# ==========================
# API KEY
# ==========================

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ==========================
# Paths
# ==========================

UPLOAD_FOLDER = "uploads"


CHROMA_PATH = os.path.join(tempfile.gettempdir(), "chroma_db")

EMBEDDING_MODEL = "mistral-embed"
LLM_MODEL = "mistral-small-latest"

TOP_K = 4
FETCH_K = 10

# ==========================
# Chunk Settings
# ==========================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# ==========================
# Models
# ==========================

EMBEDDING_MODEL = "mistral-embed"

LLM_MODEL = "mistral-small-latest"

# ==========================
# Retriever
# ==========================

TOP_K = 3

FETCH_K = 5