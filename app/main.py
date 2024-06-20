from fastapi import FastAPI
from app.api.v1.endpoints import example_controller

app = FastAPI()

app.include_router(example_controller.router, prefix="/api/v1/examples", tags=["examples"])

@app.get("/")
def read_root():
    
    return {"message": "Welcome to FastAPI"}
