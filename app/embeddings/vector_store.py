
import faiss
import numpy as np

class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def add(self, embeddings, docs):
        self.index.add(np.array(embeddings))
        self.docs.extend(docs)

    def search(self, embedding, k):
        D,I = self.index.search(embedding,k)
        return [self.docs[i] for i in I[0]]
