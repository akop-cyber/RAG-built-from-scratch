from sklearn.metrics.pairwise import cosine_similarity
class Retriever:
    """
    retrieves the appropriate and accurate datapoints
    """
    def __init__(self,vector_Store,embedder,k=5):
        self.vector_Store = vector_Store
        self.embedder = embedder
        self.k = k

    def retrieve(self,query):
        vquery = self.embedder.embed_q(query)
        stored_vectors = self.vector_Store.vectors
        scores = cosine_similarity(vquery.reshape(1,-1),stored_vectors)[0]
        top_indices = scores.argsort()[::-1][:self.k]
        
        if scores[top_indices[0]] < 0.5:
            print("Not enough evidence")
            return []

        results = [self.vector_Store.chunks[i] for i in top_indices]
        return results




