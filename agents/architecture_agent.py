import os
import json
 
from dotenv import load_dotenv
from langchain_groq import ChatGroq 

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
def generate_architecture(analysis):
    prompt=f"""

You are a Principal Software Architect.

Your job is to design architecture ONLY for the following stack:

Backend Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Validation: Pydantic
API Style: REST

IMPORTANT RULES:

You MUST use FastAPI.
You MUST use PostgreSQL.
You MUST use SQLAlchemy.
You MUST use Pydantic.
Do NOT use Spring Boot.
Do NOT use Java.
Do NOT use Node.js.
Do NOT use Express.js.
Do NOT use .NET.
Do NOT use MySQL.
Do NOT use MongoDB.

Return ONLY valid JSON.
For small and medium business applications,
prefer Monolith architecture.

Use Microservices only if explicitly required.
JSON Format:

{{
"architecture_type": "",
"backend_framework": "FastAPI",
"database": "PostgreSQL",
"modules": [],
"folder_structure": {{}},
"recommended_design_pattern": ""
}}

Requirement Analysis:

{json.dumps(analysis, indent=2)}
"""
    response=llm.invoke(prompt)
    content=response.content
    content=content.replace("```json", "")
    content=content.replace("```", "")
    content=content.strip()
    return json.loads(content)