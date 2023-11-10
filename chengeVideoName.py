# Import the os and random modules
import os
import random

# Define the source folder where the original videos are stored
src_folder = "../SampleVideos"

# Define the destination folder where the renamed videos will be stored
dst_folder = "../SampleVideos"

# Create the destination folder if it does not exist
if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

# Define a list of letters from a to z
letters = list("abcdefghijklmnopqrstuvwxyz")

# Define a counter to keep track of the new names
counter = 1

# Loop through the files in the source folder
for file in os.listdir(src_folder):
    # Get the full path of the file
    src_path = os.path.join(src_folder, file)
    # Check if the file is a video file
    if file.endswith(".mp4"):
        # Generate a random name with 4 letters
        random_name = "".join(random.choices(letters, k=4)) + ".mp4"
        # Get the full path of the random file
        random_path = os.path.join(dst_folder, random_name)
        # Rename the file by moving it to the destination folder with the random name
        os.rename(src_path, random_path)
        # Print a message to confirm the renaming
        print(f"Renamed {src_path} to {random_path}")

# Loop through the files in the destination folder
for file in os.listdir(dst_folder):
    # Get the full path of the file
    random_path = os.path.join(dst_folder, file)
    # Check if the file is a video file
    if file.endswith(".mp4"):
        # Generate the new name as counter.mp4
        new_name = f"{counter}.mp4"
        # Get the full path of the new file
        new_path = os.path.join(dst_folder, new_name)
        # Rename the file by moving it to the destination folder with the new name
        os.rename(random_path, new_path)
        # Print a message to confirm the renaming
        print(f"Renamed {random_path} to {new_path}")
        # Increment the counter
        counter += 1
