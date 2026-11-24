from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    # model="openai/gpt-oss-120b"
    model="groq/compound"
)

result = llm.invoke("write a poem")

print(result.content)