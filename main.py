import Gemini_Ai, Voice  #, Language    #, Ears
import Ears_online as Ears
import Language_online as Language
import termcolor
from pyfiglet import figlet_format
from TextProcessing import *

english_enable = False

def speak_hindi(text,from_lang="en"):
    text = Language.translate(text,from_lang=from_lang,to_lang="hi")
    Voice.speak(text)

print(termcolor.colored(figlet_format("Surya ChatBot"),"red"))

while 1:
    print("\nListening...")
    for text_voice in Ears.listen():
        if NotEmpty(text_voice) == True:
            print(text_voice)

            try:
                text_gemini = Gemini_Ai.gemini(text_voice)
                text = text_gemini.text

                print(termcolor.colored("\n\n------------------HINDI--------------\n\tCHATBOT HINDI: "+text,"green"))
                Voice.speak(text.split("\n")[0]) #("\n")[0]
                
                if english_enable == True:
                    text_translated = Language.translate(text,from_lang="hi",to_lang="en")
                    print(termcolor.colored("\n\n------------------ENGLISH--------------\n\tCHATBOT ENGLISH: "+text_translated,"green"))
            except:
                continue
