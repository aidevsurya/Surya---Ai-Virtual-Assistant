import google.generativeai as surya

surya.configure(api_key="AIzaSyBnbd_zdUgw7_R0rRuVhCq0cypEKwvTDng")
model = surya.GenerativeModel("models/gemini-pro")

user_input = ""
prompt = []

def gemini(text):
    prompt.append({"role":"user","parts":[text]})
    result = model.generate_content(prompt)
    prompt.append(result.candidates[0].content)
    return result