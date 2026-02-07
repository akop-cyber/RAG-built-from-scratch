📘 RAG from Scratch (PDF Question Answering)

This project is a Retrieval-Augmented Generation (RAG) system built completely from scratch, without using LangChain, LlamaIndex, or any external RAG framework.

The system allows users to:

Load a PDF document

Ask natural language questions

Retrieve only answers grounded in the document

Refuse to answer when the document does not contain enough evidence

🚀 Why this project?

Most RAG projects rely heavily on high-level libraries and APIs.
This project was built to understand and implement the core mechanics of RAG manually, including:

Document ingestion

Text chunking

Embedding generation

Vector storage

Similarity-based retrieval

Confidence-based refusal logic

The goal is learning + portfolio demonstration, not production deployment.

🧠 How it works (Pipeline)

Loader

Extracts raw text from PDF files

Chunker

Splits text into overlapping chunks for better semantic retrieval

Embedder

Converts text chunks into numerical vectors using
sentence-transformers/all-MiniLM-L6-v2

Vector Storage

Stores embeddings and their corresponding text chunks

Retriever

Uses cosine similarity to find the most relevant chunks

Applies a similarity threshold to avoid hallucinations

Main

Connects all components and allows interactive querying

❌ Hallucination Control

If the similarity score of the best matching chunk is below a threshold (default: 0.5), the system refuses to answer and reports that there is not enough evidence in the document.

This ensures answers are source-grounded.

🧪 Example Output
Enter your query: Why were people angry with the Weimar Republic?

Answer based on the document:

1. easantry was affected by a sharp fall in agricultural prices and women, unable to fill their children’s stomachs, were filled with a sense of deep despair. Politically too the Weimar Republic was fragile. The Weimar constitution had some inherent defects, which made it unstable and vulnerable to dictatorship. One was proportional representation. This made achieving a majority by any one party a near impossible task, leading to a rule by coalitions. Another defect was Article 48, which gave the

2. ve an opportunity to parliamentary parties to recast German polity. A National Assembly met at Weimar and established a democratic constitution with a federal structure. Deputies were now elected to the German Parliament or Reichstag, on the basis of equal and universal votes cast by all adults including women. This republic, however, was not received well by its own people largely because of the terms it was forced to accept after Germany’s defeat at the end of the First World War. The peace t

3. porary World 521.1 The Effects of the War The war had a devastating impact on the entire continent both psychologically and financially. From a continent of creditors, Europe turned into one of debtors. Unfortunately, the infant Weimar Republic was being made to pay for the sins of the old empire. The republic carried the burden of war guilt and national humiliation and was financially crippled by being forced to pay compensation. Those w ho suppor ted the Weimar R epublic, mainl y Socialists ,

4. e for not onl y the defeat in the w ar but the disg race at Versailles . Reprint 2025-26 Nazism and the Rise of Hitler 53in many cities. The political atmosphere in Berlin was charged with demands for Soviet-style governance. Those opposed to this – such as the socialists, Democrats and Catholics – met in Weimar to give shape to the democratic republic. The Weimar Republic crushed the uprising with the help of a war veterans organisation called Free Corps. The anguished Spar tacists la ter found

5. reduce rapidly. Aggressive war propaganda and national honour occupied centre stage in the public sphere, while popular support grew for conservative dictatorships that had recently come into being. Democracy was indeed a young and fragile idea, which could not survive the instabilities of interwar Europe. 1.2 Political Radicalism and Economic Crises The birth of the Weimar Republic coincided with the revolutionary uprising of the Spartacist League on the pattern of the Bolshevik Revolution in

🛠️ Technologies Used

Python

Sentence Transformers

Cosine Similarity (scikit-learn)

PyPDF2

NumPy

📌 Notes

This project does not use an LLM yet

The focus is on retrieval, which is the hardest and most important part of RAG

LLM-based answer generation may be added in a future version

🧑‍💻 Author





Built by Aarav
(Student | AI & ML Enthusiast)











