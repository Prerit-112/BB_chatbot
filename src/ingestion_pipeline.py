from document_loader import DocumentLoader
from chunker import chunk_documents
import nltk

required_packages = [
    "punkt",
    "averaged_perceptron_tagger",
    "wordnet",
    "stopwords",
    "maxent_ne_chunker",
    "words"
]

for pkg in required_packages:
    nltk.download(pkg)


def run_ingestion_pipeline(manifest_path, data_path, chunk_size=1000, chunk_overlap=100):
    print("Loading documents...")
    loader = DocumentLoader(manifest_path, data_path)
    documents = loader.load_pdfs()
    print(f"Loaded {len(documents)} documents.")

    print("Chunking documents...")
    chunks = chunk_documents(documents, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    print(f"Created {len(chunks)} chunks.")

    # Ready for embedding or saving to a file/vector store, etc.
    return chunks

if __name__ == "__main__":
    MANIFEST_PATH = "configs/manifest.json"      # Adjust path if running from repo root
    DATA_PATH = "../drive/My Drive/BB_chatbot/data/sgi_newsletter"
    chunks = run_ingestion_pipeline(MANIFEST_PATH, DATA_PATH)
    # Optionally: Save to disk, or print preview
    print(chunks[0] if chunks else "No chunks generated.")
