from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

vectors = embeddings.embed_documents(
    [
        "today is monday",
        "today is tuesday",
        "today is april fools day"
    ]
)

print(len(vectors),len(vectors[2]))