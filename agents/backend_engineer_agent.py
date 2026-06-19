import os
import json

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_backend_code(architecture):

    with open(
        "agents/prompts/backend_engineer_prompt.txt",
        "r",
        encoding="utf-8"
    ) as f:

        prompt_template = f.read()

    prompt = prompt_template.replace(
        "{architecture}",
        json.dumps(
            architecture,
            indent=2
        )
    )

    response = llm.invoke(prompt)

    content = response.content

    content = content.replace(
        "```python",
        ""
    )

    content = content.replace(
        "```",
        ""
    )

    content = content.strip()

    return content