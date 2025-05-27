def speech_file(mytext="Hello World", output_file="output", voice= "tts_models/en/blizzard2013/capacitron-t2-c50"):
    import torch
    from TTS.api import TTS

    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # List available 🐸TTS models
    print(TTS().list_models())

    # Init TTS with the target model name
    tts = TTS(model_name = voice, progress_bar=False).to(device)

    # Run TTS
    tts.tts_to_file(text = mytext, file_path = output_file)

    # # Example voice cloning with YourTTS in English, French and Portuguese
    # tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
    # tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
    # tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr-fr", file_path="output.wav")
    # tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt-br", file_path="output.wav")