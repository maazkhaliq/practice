from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver

llm=ChatGoogleGenerativeAI(
    api_key='API_KEY',
    model='gemini-2.5-flash',
    temperature=0,
    max_retries=2,
    max_tokens=None,
    timeout=None

)



memory=InMemorySaver()

memory_agent=create_agent(
    model=llm,
    
    system_prompt='You are a helpfull assistant,answer all type of questions intelligently and warmly,sensitive questions with deep research',
    checkpointer=memory
)