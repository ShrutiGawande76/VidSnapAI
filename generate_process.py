import os 
from text_to_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    print("TTA - ", folder)

    desc_path = os.path.join("user_uploads", folder, "desc.txt")

    if not os.path.exists(desc_path):
        print(f"desc.txt missing for {folder}, skipping audio generation")
        return False

    with open(desc_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    print(text, folder)
    text_to_speech_file(text, folder)
    return True


def create_reel(folder):
    command = f''' Your_Folder_command'''
    subprocess.run(command, shell=True, check=True)
    print("CR - ", folder)


if __name__ == "__main__":
    while True:
        print("Processing queue...")

        with open("done.txt", "r") as f:
            done_folders = [line.strip() for line in f.readlines()]

        folders = os.listdir("user_uploads")

        for folder in folders:
            if folder not in done_folders:
                audio_created = text_to_audio(folder)

                if audio_created:
                    create_reel(folder)
                    with open("done.txt", "a") as f:
                        f.write(folder + "\n")
                else:
                    print(f"Skipping reel creation for {folder}")

        time.sleep(4)



