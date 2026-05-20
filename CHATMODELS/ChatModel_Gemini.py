from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

chat_model = GoogleGenerativeAI(model='gemini-1.5-pro')

result = chat_model.invoke("who is the prime minister of INDIA")

print(result.content)