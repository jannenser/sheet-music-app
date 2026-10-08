from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(title="Audio Processor API")

app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "Welcome to Audio Processor!"}