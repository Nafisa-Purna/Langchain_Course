from langchain_google_genai import ChatGoogleGenerativeAI  
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

resutl = model.invoke("What is the capital of Banladesh")

print(result.content)