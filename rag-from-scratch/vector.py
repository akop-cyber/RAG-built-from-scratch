class VectorStorage:
    """
    stores the datapoint or the vectors
    """

    def __init__(self):
        self.vectors = []
        self.chunks = []

    def add(self,vectors,chunks):
        if len(vectors) == len(chunks):
            for i in range(len(chunks)):
                self.vectors.append(vectors[i])
                self.chunks.append(chunks[i])

        else:
            raise ValueError("Length of vectors do not match the lenght of the chunk")
        
    def __len__(self):
        return len(self.chunks)