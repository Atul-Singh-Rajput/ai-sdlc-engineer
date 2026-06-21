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

Return ONLY VALID JSON.

DO NOT write explanations.
DO NOT write markdown.
DO NOT write text before JSON.
DO NOT write text after JSON.

IMPORTANT JSON RULES:

1. Every key must have a value.
2. Use only JSON objects {{}} and JSON arrays [].
3. Never generate structures like:

{{
  "employee.py",
  "department.py"
}}

This is INVALID.

Use:

{{
  "models": [
    "employee.py",
    "department.py"
  ]
}}

OR

{{
  "models": {{
    "employee.py": "Employee model",
    "department.py": "Department model"
  }}
}}

4. The response must be parseable by json.loads().
5. Start response with an opening curly brace.
6. End response with a closing curly brace.

Return EXACTLY this structure:

{{
  "architecture_type": "Monolith",
  "backend_framework": "FastAPI",
  "database": "PostgreSQL",
  "modules": [],
  "folder_structure": {{
    "app": {{
      "models": [],
      "schemas": [],
      "routes": [],
      "services": [],
      "repositories": []
    }}
  }},
  "recommended_design_pattern": ""
}}

Requirement Analysis:

{{json.dumps(analysis, indent=2)}}
The modules MUST be derived from the entities and features in the requirement analysis.

Example:

If entities contain Employee and Report:

modules should contain:
[
  "employees",
  "reports",
  "authentication"
]

Do not generate unrelated modules such as:
users,
products,
orders

unless they are explicitly mentioned in the requirement analysis.
"""
    response=llm.invoke(prompt)
    content = response.content

    content = content.replace(
        "```json",
        ""
    )

    content = content.replace(
        "```",
        ""
    )

    content = content.strip()

    print("\n========== ARCHITECTURE RESPONSE ==========\n")
    print(content)
    print("\n========== END RESPONSE ==========\n")

    # Extract only JSON portion

    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:

        raise Exception(
            "No JSON found in architecture response"
        )

    content = content[start:end + 1]

    try:
        return json.loads(content)

    except Exception as e:
        print("\nJSON PARSE FAILED\n")
        print(content)
        raise e