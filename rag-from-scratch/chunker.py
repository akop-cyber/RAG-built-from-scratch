class Chunker:
    """
    devides the files in seprate chunks manually
    """
    def __init__(self,chunk_size=500,overlap = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap
        

    def chunker(self,text):
        if self.overlap >= self.chunk_size or self.overlap == self.chunk_size:
            print("Overlap size cant be greater or equall to chunk_size")
        elif self.overlap < self.chunk_size:
            chunks = []
            start = 0
            text_size = len(text)
            while start < text_size:
                end = start + self.chunk_size
                chunk = text[start:end]
                if chunk.strip():
                    chunks.append(chunk)
                start = start + self.chunk_size - self.overlap
        return chunks