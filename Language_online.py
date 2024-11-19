from deep_translator import GoogleTranslator
Translator = GoogleTranslator(source="auto",target="en")

def translate(text,from_lang="en",to_lang="hi"):
    return Translator.translate(text,from_code=from_lang,to_code=to_lang)