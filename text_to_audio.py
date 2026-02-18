import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

client = ElevenLabs(api_key="sk-123456")


def text_to_speech_file(text: str, folder: str) -> str:

    # Generate audio
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    folder_path = os.path.join("user_uploads", folder)
    os.makedirs(folder_path, exist_ok=True)

    # Audio file path
    save_file_path = os.path.join(folder_path, "audio.mp3")

    # Save audio file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print("Audio saved at:", os.path.abspath(save_file_path))

    return save_file_path

if __name__ == "__main__":
    text_to_speech_file(
        "Hey I am Shruti and its the python course",
        "Folder path"
    )




