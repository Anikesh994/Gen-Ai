from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4' , temperature =0)

result = chat_model.invoke('hello how are u ')

print(result.content)