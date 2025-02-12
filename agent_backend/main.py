import uvicorn

from agent_api.api import app
from agent import Agent

if __name__ == "__main__":
    # Initialize the Agent
    agent = Agent()
    agent.startAgent()
    
    # Start the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)