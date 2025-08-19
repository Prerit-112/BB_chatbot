from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    all_chunks = []
    for doc in documents:
        chunks = text_splitter.split_text(doc["text"])
        for idx, chunk_text in enumerate(chunks):
            chunk = {
                "chunk_text": chunk_text,
                "chunk_index": idx,
                "metadata": doc["metadata"]
            }
            all_chunks.append(chunk)
    return all_chunks
