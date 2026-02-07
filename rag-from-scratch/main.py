from loader import Loader
from chunker import Chunker
from embedder import Embedder
from vector import VectorStorage
from retriever import Retriever
from cleaner import clean_text
import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity

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
