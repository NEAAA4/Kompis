import speech_recognition as sr
import pyttsx3
import ollama

"""AI KODGENERERAT DELUXE"""

# 1. Förbered Röstmotorn (Text-till-Tal)
engine = pyttsx3.init()
engine.setProperty('rate', 160) # Justera talhastigheten

def prata(text):
    print(f"\nAssistenten: {text}")
    engine.say(text)
    engine.runAndWait()

# 2. Förbered Öronen (Tal-till-Text)
recognizer = sr.Recognizer()

def lyssna():
    with sr.Microphone() as source:
        print("\n[Lyssnar... Prata nu]")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Vi använder Google gratis-API för snabb och enkel start.
            text = recognizer.recognize_google(audio, language="sv-SE")
            print(f"Du sa: {text}")
            return text
        except sr.UnknownValueError:
            print("[Hörde inte vad du sa]")
            return ""
        except sr.RequestError:
            print("[Kunde inte ansluta till tal-igenkänningen]")
            return ""

# 3. Huvudprogrammet
prata("Hej! Jag är redo att prata.")

while True:
    användarens_text = lyssna()
    
    # Säg "avsluta" för att stänga programmet
    if "avsluta" in användarens_text.lower():
        prata("Hejdå! Vi hörs.")
        break
        
    if användarens_text:
        # Byt ut 'llama3.2' mot namnet på modellen du laddade ner
        response = ollama.chat(model='llama3.2', messages=[
          {'role': 'user', 'content': användarens_text}
        ])
        
        svar = response['message']['content']
        prata(svar)