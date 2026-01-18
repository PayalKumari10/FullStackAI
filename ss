#Chain of Thought Prompting 

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """ 
 You're an expert AI Assistant in resolving user queries using chain of thought 
 You work on START, PLAN and OUTPUT stpes.
 You need to first PLAN what needs to be done, finally you cn give an OUTPUT.

 Rules:
 - Stricitly Follow the given JSON output format 
 - Only run one step at a time.
 - The sequence of step is START (where user gives an input), PLAN(That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

 Output JSON Format:
 { "stop": "START" |"PLAN" | "OUTPUT": "string"}
 
 Example:
 START: Hey, Can you solve 2 + 3 * 5 / 10
 PLAN: {"step": "PLAN": "contnet": "Seems like user is intersted in math problem"}
 PLAN: {"step": "PLAN": "contnet": "looking at the probelm, we should solve this using BODMAS method"}
 PLAN: {"step": "PLAN": "contnet": "Yes, The BODMAS is correct thing to done here"}
 PLAN: {"step": "PLAN": "contnet": "first we must multiply 3 * 5 which is 15"}
 PLAN: {"step": "PLAN": "contnet": "Now the new equation is 2 + 15 / 10"}
 PLAN: {"step": "PLAN": "contnet": "We must perfrom divide that is 15 / 10 = 1.5"}
 PLAN: {"step": "PLAN": "contnet": "Now the new equation is 2 + 1.5"}
 PLAN: {"step": "PLAN": "contnet": "Now finally lets perform the add "}
 PLAN: {"step": "PLAN": "contnet": "Great, we have solved and final with 3.5 as ans"}
 OUTPUT: {"step": "OUTPUT": "content": "3.5"}

 """

 message_history = [
    {
        "role": "system", "content": SYSTEM_PROMPT
    },
 ]

 user_query = input("👉")
 message_histroy.append({"role": "user", "content": user_query})

 while True:
     response = client.chat.completions.create (
         model="gemini-3-flash-preview",
         response_format={"type":"json_object"},
         messages = message_history
     )
    
    raw_result = (response.choices[0].message.content)
    message_history.append("role": "assistant", "content": raw_result)
    
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
       print("🔥", parased_result.get("content"))
       continue

    if parsed_result.get("step") == "PLAN":   
       print("🧠", parased_result.get("content"))
       continue
    
    if parsed_result.get("step") == "PLAN":   
       print("🤖", parased_result.get("content"))
       break

print("\n\n\n")


