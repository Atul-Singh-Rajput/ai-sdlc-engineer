import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from agents.requirement_agent import analyze_requirement
from agents.architecture_agent import generate_architecture
from agents.orchestrator_agent import run_pipeline

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
        architecture = generate_architecture(result)
        os.makedirs("generated_projects", exist_ok=True)
        with open("generated_projects/requirement.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)
        with open("generated_projects/architecture.json", "w", encoding="utf-8") as f:
            json.dump(architecture, f, indent=4)


        return {
            "requirement_analysis": result,
            "architecture": architecture
        }
    except Exception as e:
        return {
            "error": str(e)
        }
@app.post("/generate-project")
def generate_project(data: dict):

    requirement = data["requirement"]

    result = run_pipeline(
        requirement
    )

    return result