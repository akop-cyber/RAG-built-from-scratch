from loader import Loader
from chunker import Chunker
from embedder import Embedder
from vector import VectorStorage
from retriever import Retriever
from cleaner import clean_text
import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity
#You can load any pdf you want by adding the file address for reference. I have provided a pdf 
#This model works on text only pdf and can crash on poorly scaned pdf files or image files
text = Loader("nazi.pdf")
text_ = text.load()
chunk = Chunker()
chunks = chunk.chunker(text_)
#print(len(chunks))
#print(chunks[0][:200])

e = Embedder()
v = e.embed(chunks)

store = VectorStorage()
print(len(store))

store.add(v,chunks)
print(len(store))

ret = Retriever(store,e)

query = input("Enter your query: ")

answer = ret.retrieve(query)

print("\nAnswer based on the document:\n")

for i, chunk in enumerate(answer, 1):
    cleaned = clean_text(chunk)
    print(f"{i}. {cleaned}\n")

