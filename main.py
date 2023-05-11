from dotenv.main import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.environ['API_KEY']

prompt = "Write me a conclusion of an article talking about the use of the ChatGPT api"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}])

print(completion['choices'][0]['message']['content'])
