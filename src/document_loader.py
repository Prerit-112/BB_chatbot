from unstructured.partition.pdf import partition_pdf
import os
import json

class DocumentLoader:
    def __init__(self, manifest_path, gdrive_data_path):
        self.manifest_path = manifest_path
        self.gdrive_data_path = gdrive_data_path
        self.manifest = self._load_manifest()

    def _load_manifest(self):
        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def load_pdfs(self):
        documents = []
        pdf_entries = self.manifest.get("pdfs", {}).get("files", [])

        for entry in pdf_entries:
            filename = entry.get("title")
            file_path = os.path.join(self.gdrive_data_path, filename)

            if not os.path.isfile(file_path):
                # Optional: Add download logic here if PDF missing locally
                print(f"Warning: PDF file missing locally: {file_path}")
                continue

            elements = partition_pdf(filename=file_path)
            # Extract text pages preserving page number & sections (Unstructured.io returns elements with metadata)

            full_text = "\n\n".join([el.text for el in elements if el.text])
            metadata = {
                "title": entry.get("title"),
                "url": entry.get("url"),
                "source": entry.get("source"),
                "topics": entry.get("topics", []),
                "tags": entry.get("tags", []),
                "description": entry.get("description"),
                "file_path": file_path,
            }
            documents.append({"text": full_text, "metadata": metadata})
        return documents
