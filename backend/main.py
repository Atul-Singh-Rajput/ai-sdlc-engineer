from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def home():
    return{ "status":"running"}

@app.post("/generate")
def generate():
    return {"message":"working....."}
