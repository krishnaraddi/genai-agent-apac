from fastapi import FastAPI, Request
from app.agent import SummarizerAgent

app = FastAPI()
agent = SummarizerAgent()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}
    
    summary = agent.run(text)
    return {"summary": summary}