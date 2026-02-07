from sentence_transformers import SentenceTransformer
class Embedder:
    """
    converts the text into numbers 
    and places them close meaningfully
    """
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


    def embed(self,chunk):
        vectors = self.model.encode(chunk)
        return vectors
    
    def embed_q(self,query):
        q_vector = self.model.encode(query)
        return q_vector


