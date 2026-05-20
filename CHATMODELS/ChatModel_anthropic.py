from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model='claude-3.5-sonnet')

result = chat_model.invoke("who is the prime minister of INDIA")

print(result.content)