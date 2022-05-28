import openai
from env import access_secret

# load openai key
openai.api_key = access_secret('LINK_TO_SECRET')
completion = openai.Completion()

# chat initiation
start_chat_log = '''Human: Hello, how are you?
AI: I am doing great. What's up?
'''

# GPT-3 query
def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine='text-davinci-002', stop=['\nHuman:'], temperature=0.1,
        top_p=1, frequency_penalty=0.0, presence_penalty=0.0, best_of=1,
        max_tokens=100)
    answer = response.choices[0].text.strip()
    return answer
