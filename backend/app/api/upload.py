from fastapi import APIRouter, UploadFile, File
from app.services.processor import process_music

router = APIRouter()


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    return await process_music(file)