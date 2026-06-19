import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_requirement(requirement):
    prompt= f"""
    You are a Senior Solution Architect.

    Analyze the software requirement.

    Extract:
    - Project Name
    - Project Type
    - Entities
    - Roles
    - Features
    - API Endpoints

    Return valid JSON only.

    Requirement:
    {requirement}
    """

    response= llm.invoke(prompt)
    content = response.content
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()
    return json.loads(content)