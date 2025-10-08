import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"
messages = [
  {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]
payload = {
  "model": MODEL,
  "messages": messages,
  "stream": False
}
response = ollama.chat(MODEL, messages)
print(response['message']['content'])