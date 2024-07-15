from ollama_model import get_vector_ollama, get_single_completion_ollama, stream_a_completion_ollama

# SPECIfY MODELS in ollama_model.py then run main.py

if __name__ == '__main__':
   
   ## create an embedding -->
    # vector = get_vector_ollama("hello")

   ## create a single response -->
    # response = get_single_completion_ollama("say something")

   ## stream a response -->
    response_stream = stream_a_completion_ollama("tell me a short story")
    
    for chunk in response_stream:
        print(chunk['message']['content'], end='', flush=True)
    