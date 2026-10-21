import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
claude_api_key = os.getenv('ANTHROPIC_API_KEY')


# Check the OpenAI key
if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

# Check the Anthropic key
if not claude_api_key:
    print("No Anthropic API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not claude_api_key.startswith("sk-ant-"):
    print("An Anthropic API key was found, but it doesn't start sk-ant-; please check you're using the right key - see troubleshooting notebook")
elif claude_api_key.strip() != claude_api_key:
    print("An Anthropic API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("Anthropic API key found and looks good so far!")


openai = OpenAI()
client = Anthropic()


system_prompt = "You are a Spanish history teacher."
user_prompt = "Give me an interesting fact about Puerto Rico."

#Setting up the LLM call as a function
def call_gpt(prompt):
    #See Week 2, Day 3 for context on chat history initialization
    chat_history = [
        {"role": "assistant", "content": ""}
    ]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            *chat_history,
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

#print(response.choices[0].message.content) // OpenAI print of response

print("GPT response:", call_gpt(user_prompt))

"""
#CLAUDE variant
def call_claude(prompt):
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.content[0].text

print("Claude response:", call_claude(user_prompt))

#print(response.content[0].text) //Claude print of response
"""