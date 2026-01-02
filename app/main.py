from fastapi import FastAPI
from dotenv import load_dotenv
from .vector_store import initialize_guidelines
from .agents import care_coordinator_agent

load_dotenv()
app = FastAPI(title="Clinical AI Agent")

retriever = initialize_guidelines()

@app.post("/coordinate")
async def coordinate_care(patient_json: dict):
    # 1. RAG: Get relevant guidelines
    guidelines = retriever.get_relevant_documents("Check patient vitals and meds")
    context = "\n".join([d.page_content for d in guidelines])
    
    # 2. Agent Logic
    response = care_coordinator_agent(str(patient_json), context)
    
    return {
        "status": "Success",
        "agent_output": response.content,
        "human_approval_required": True
    }