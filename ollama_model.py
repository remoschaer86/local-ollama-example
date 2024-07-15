import ollama
from ollama import Client

EMBEDDINGS_MODEL= "nomic-embed-text:latest"
CHAT_MODEL = "llama3"


def get_vector_ollama(text):
  try:    
    res = ollama.embeddings(model=EMBEDDINGS_MODEL, prompt=text)
    return res["embedding"]
  except ollama.ResponseError as e:
    print(e.error)
    return None


def get_single_completion_ollama(text):
  try:  
    response = ollama.chat(model=CHAT_MODEL, messages=[
    {
        'role': 'user',
        'content': text,
    },
    ])
    return response['message']['content']  
  except ollama.ResponseError as e:
    print(e.error)
    return None
  
# does not exist in retos code
def stream_a_completion_ollama(text):
  try:  
    stream = ollama.chat(
      model='llama3',
      messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
      stream=True,
    ) 
    return stream
  except ollama.ResponseError as e:
    print(e.error)
    return None



## reto uses the following function as well in his code. I would probably have to adapt his code to integrate it
# def get_completion_openai(**args):

#     if not check_key():

#         return None

#     client = OpenAI()

#     args["model"] = CHAT_MODEL

#     chat_completion = client.chat.completions.create(**args)

#     return chat_completion

 


