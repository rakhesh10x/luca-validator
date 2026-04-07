import sys
import os

# Path fix
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("./agents"))
os.environ["PYTHONPATH"] = os.path.abspath(".")

print("✅ PYTHONPATH set successfully")
print("Current path:", os.path.abspath("."))

from fastapi import FastAPI
from pydantic import BaseModel
from langgraph_workflow import run_validation_pipeline
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="10X LangGraph Agentic Validation System - LUCA V3",
    description="Dynamic Rule-Driven SFT/Data File Validation Tool"
)

class ValidationRequest(BaseModel):
    drive_link: str
    rule_sets: dict

@app.post("/validate")
async def validate(request: ValidationRequest):
    report = await run_validation_pipeline(request.drive_link, request.rule_sets)
    return report

if __name__ == "__main__":
    print("🚀 Starting LUCA V3 Validation Server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)