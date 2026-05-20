from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result =llm.invoke(" who is Nikola Tesla")


print(result)


# llms take's a string as input and return a string as output

# IN PRESENT TIMES DEVELOPER HAVE MOVED TO CHAT MODELS