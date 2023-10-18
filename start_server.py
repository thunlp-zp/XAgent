import uvicorn

from XAgentServer.envs import XAgentServerEnv

if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1",
                port=XAgentServerEnv.port, reload=XAgentServerEnv.reload, workers=XAgentServerEnv.workers)