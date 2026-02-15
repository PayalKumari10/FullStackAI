from dotenv import load_dotenv

import speech_recognition as sr
from openai import OpenAI

load_dotenv()

client = OpenAI()

def main():
    r = sr.Recognizer() #Speech to Text

    with sr.Microphone() as source: #Mic Access
        r.adjust_for_ambient_noise(source) #Noise Reduction
        r.pause_threshold = 2 #Pause Threshold

        print("Speak Something...")
        audio = r.listen(source)

        print("Processing Audio... (STT)")
        stt = r.recognize_google(audio) #Google STT

        print("You Said:", stt)

        SYSTEM_PROMPT = f"""
             you are an expert voice agent. You are given the transcript pf what
             user has said using voice.
             You need to output as if you are voice agent and whatever yu speak 
             will be converted back to audio usinf AI and played back to user.
        """     

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt}
            ]
        )

        print("AI Respones", response.choices[0].message.content)
main()