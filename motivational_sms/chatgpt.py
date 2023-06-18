import openai
from config import OPENAI_KEY
from long_prompts import DAN_PRIMER, DAN_RESPONSE

openai.api_key = OPENAI_KEY

def generate_tier1_reachout(personality: str = ""):
    prompt = "A very short motivational message to get someone to start working"
    if personality:
        prompt += f" in the style of {personality}"
    prompt += ":\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response.choices[0].text

def dan(prompt: str):
    messages = [
        {"role": "user", "content": DAN_PRIMER},
        {"role": "assistant", "content": DAN_RESPONSE},
        {"role": "user", "content": prompt},
    ]
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    return chat.choices[0].message["content"].split("JAILBREAK: ")[1]