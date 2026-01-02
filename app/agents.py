from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def care_coordinator_agent(patient_data, clinical_context):
    prompt = ChatPromptTemplate.from_template("""
    You are a Clinical AI Care Coordinator.
    
    PATIENT HISTORY: {patient_data}
    CLINICAL GUIDELINES: {clinical_context}
    
    Task:
    1. Summarize the patient's current status.
    2. Identify any alerts (deviations from guidelines).
    3. Propose a next-step care plan.
    4. Provide 'Reasoning' for every recommendation (Explainable AI).
    
    Constraint: If data is missing, state 'Insufficient data'. Do not hallucinate.
    """)
    
    chain = prompt | llm
    return chain.invoke({
        "patient_data": patient_data,
        "clinical_context": clinical_context
    })