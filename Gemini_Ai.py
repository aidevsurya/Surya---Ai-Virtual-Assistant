import google.generativeai as surya

api_key = "[REPLACE BY YOURS]"

surya.configure(api_key=api_key)
model = surya.GenerativeModel("models/gemini-pro")

user_input = ""
prompt = []

def gemini(text):
    prompt.append({"role":"user","parts":[text]})
    result = model.generate_content(prompt)
    prompt.append(result.candidates[0].content)
    return result