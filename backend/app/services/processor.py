from pathlib import Path
import uuid
import shutil
from backend.app.processing.audio import process_audio
from fastapi import UploadFile


UPLOAD_FOLDER = Path("uploads")
OUTPUT_FOLDER = Path("outputs")

UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)


async def process_music(file: UploadFile):

    # create unique job
    job_id = str(uuid.uuid4())[:8]

    upload_dir = UPLOAD_FOLDER / job_id
    output_dir = OUTPUT_FOLDER / job_id

    upload_dir.mkdir()
    output_dir.mkdir()

    # save original file
    original_file = upload_dir / file.filename

    with open(original_file, "wb") as buffer:
        buffer.write(await file.read())

    # dummy processing:
    # copy the same MP3 as the "processed" file
    # processed_file = output_dir / f"processed_{file.filename}"

    processed_audio_files = process_audio(output_dir, file.filename)

    shutil.copy(
        original_file,
        processed_audio_files
    )


    return {
        "job_id": job_id,
        "original": str(original_file),
        "processed_file": str(processed_file)
    }