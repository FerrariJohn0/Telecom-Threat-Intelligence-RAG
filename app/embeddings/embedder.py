
from sentence_transformers import SentenceTransformer

class Embedder:

    def __init__(self, model):
        self.model = SentenceTransformer(model)

    def encode(self,texts):
        return self.model.encode(texts)
