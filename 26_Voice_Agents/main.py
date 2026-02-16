import asyncio
from openai import AsyncOpenAI
# from audio import LocalAudioPlayer


from dotenv import load_dotenv

import speech_recognition as sr
from openai import OpenAI

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_resposne.create(
        # model="gpt-4o-mini-tts",
        model="gpt-4.1-mini",
        voice="coral",
        instrution="Always speak in cherfull manner with full of delight and happy",
        input=speech
    )as response:
        await LocalAudioPlayer().play(response) 

def main():
    r = sr.Recognizer() #Speech to Text

    with sr.Microphone() as source: #Mic Access
        r.adjust_for_ambient_noise(source) #Noise Reduction
        r.pause_threshold = 2 #Pause Threshold
        SYSTEM_PROMPT = f"""
             you are an expert voice agent. You are given the transcript pf what
             user has said using voice.
             You need to output as if you are voice agent and whatever yu speak 
             will be converted back to audio usinf AI and played back to user.
        """  
        messages= [{"role": "system", "content": SYSTEM_PROMPT},]

    while True:

        print("Speak Something...")
        audio = r.listen(source)

        print("Processing Audio... (STT)")
        stt = r.recognize_google(audio) #Google STT

        print("You Said:", stt)

        messages.append( {"role": "user", "content": stt}
          )   

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )

        print("AI Respones", response.choices[0].message.content)
        asyncio.run(tts(speech=response.choices[0].message.content))

main()