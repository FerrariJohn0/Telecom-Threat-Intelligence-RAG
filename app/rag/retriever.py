
class Retriever:

    def __init__(self,embedder,store):
        self.embedder = embedder
        self.store = store

    def retrieve(self,query,k):
        q = self.embedder.encode([query])
        return self.store.search(q,k)
