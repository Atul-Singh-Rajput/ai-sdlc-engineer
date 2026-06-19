import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from agents.requirement_agent import analyze_requirement
app=FastAPI()
@app.get("/")
def home():
    return{ "status":"running"}

@app.post("/generate")
def generate():
    return {"message":"working....."}

class RequirementRequest(BaseModel):
    requirement: str

@app.post("/analyze-requirement")
def analyze(req: RequirementRequest):
    try:
        result = analyze_requirement(
            req.requirement
        )
        os.makedirs("generated_projects", exist_ok=True)
        with open("generated_projects/output.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)


        return result
    except Exception as e:
        return {
            "error": str(e)
        }
