from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save

def generate_xml(output_directory, input_audio_path):

    # Ensure the input file exists
    if not os.path.exists(input_audio_path):
        raise FileNotFoundError(f"Error: The file '{input_audio_path}' does not exist.")

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Load the model path
    model_path = str(ICASSP_2022_MODEL_PATH)

    print(f"Starting transcription of {input_audio_path}...")

    # Run the prediction and save the MIDI file
    # NOTE: The function signature expects positional arguments for the first few parameters.
    predict_and_save(
        [input_audio_path],  # Positional Arg 1: audio_path_list
        output_directory,  # Positional Arg 2: output_directory
        True,  # Positional Arg 3: save_midi
        False,  # Positional Arg 4: sonify_midi
        False,  # Positional Arg 5: save_model_outputs
        False,  # Positional Arg 6: save_notes
        model_or_model_path=model_path  # Use the correct keyword argument
    )

    print(f"Transcription complete. MIDI file saved in: {output_directory}")

    midi_file_path = os.path.join(output_directory, input_audio_path)
    # Convert the MIDI file to a music21 stream object
    score = converter.parse(midi_file_path)

    # You can now analyze or save this score in MusicXML format
    # This might require a program like MuseScore installed on your system to render visually
    score.write('musicxml', fp=os.path.join(output_directory, 'shouldistay_bass_music.xml'))