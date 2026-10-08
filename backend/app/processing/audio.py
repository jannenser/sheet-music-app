import os

def process_audio(output_dir, file_path) -> list():
    pip install demucs
    !demucs "file_path"
    output_dir = f"separated/htdemucs/{os.path.splitext(filename)[0]}"
    vocals_path = os.path.join(output_dir, "vocals.wav")
    bass_path = os.path.join(output_dir, "bass.wav")
    drums_path = os.path.join(output_dir, "drums.wav")
    other_path = os.path.join(output_dir, "other.wav")
    return [vocals_path,bass_path,drums_path,other_path]