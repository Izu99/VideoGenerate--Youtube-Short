import os

def delete_file():
    current_directory = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the Python script
    extensions_to_delete = [".mp4", ".wav", ".mp3"]
    files_to_exclude = ["final_video.mp4", "silence.wav", "utubeShort.exe"]

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Iterate through the files and delete the ones with specified extensions, excluding the files_to_exclude
    for file in files:
        if file not in files_to_exclude and any(file.endswith(ext) for ext in extensions_to_delete):
            file_path = os.path.join(current_directory, file)
            os.remove(file_path)
            print(f"File '{file}' has been deleted.")

    print("Deletion of files with specified extensions is complete.")

if __name__ == "__main__":
    delete_file()
