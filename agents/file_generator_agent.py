import json
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY1")
)

def generate_file(filepath, architecture):
    with open(
        "agents/prompts/file_generator_prompt.txt",
        "r",
        encoding="utf-8"
    ) as f:

        prompt = f.read()
    prompt = prompt.replace(
        "{filepath}", filepath)
    
    prompt=prompt.replace(
        "{architecture}",
        json.dumps(
            architecture,
            indent=2
        )
    )

    response=llm.invoke(prompt)
    content=response.content
    content=content.replace("```python","")
    content=content.replace("```","")
    content=content.strip()
    return content