import os

# specify the file path
file_path = '../SampleAudios/no1.mp3'

# check if the file exists
if os.path.exists(file_path):
    # delete the file
    os.remove(file_path)
    print("File deleted.")
else:
    print("The file does not exist.")
