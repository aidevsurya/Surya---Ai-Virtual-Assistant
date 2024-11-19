from llama_cpp import Llama

# model = r"D:\Suryansh\Workspace\AI\Surya\models\Meta-Llama-3.1-8B-Instruct_CODE_Python_English_Asistant-16bit.gguf"
# model = r"D:\Suryansh\Workspace\AI\Surya\models\GPT-Sw3-126M-f32-GGUF.gguf"
# model = r"D:\Suryansh\Workspace\AI\Surya\models\gpt-sw3-6.7b-v2-Q5_K_M.gguf"
model = r"D:\Suryansh\Workspace\AI\Surya\models\llama-2-7b-chat.Q5_K_M.gguf"
context_size = 512

llama_model = Llama(model,n_ctx=context_size)

def chat(text,max_tokens=60,temperature=0.4,top_k=30,top_p=0.8,echo=True,stop=["\n"]):
    text = llama_model(text,max_tokens=max_tokens,temperature=temperature,top_k=top_k,top_p=top_p,echo=echo,stop=stop)
    return text["choices"][0]["text"]