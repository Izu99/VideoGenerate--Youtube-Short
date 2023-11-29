import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip

def get_random_video():
    video_folder = '../SampleVideos'  # The path to your video folder
    videos = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]
    # random_video = "22.mp4"
    random_video = random.choice(videos)
    video_path = os.path.join(video_folder, random_video)

    # Get the duration of the video in seconds
    clip = VideoFileClip(video_path)
    duration = clip.duration

    return video_path, duration

video_path, duration = get_random_video()
print(f"Video path: {video_path}")
print(f"Duration in seconds: {duration}")

# Load your video
video = VideoFileClip(video_path)
# specify the directory where the mp3 files are located

directory = '../SampleAudios/'

# get a list of all mp3 files in the directory
mp3_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]

# select a random mp3 file
random_file = random.choice(mp3_files)

# create the full path of the random mp3 file
random_file_path = os.path.join(directory, random_file)

# pass the random mp3 file to AudioFileClip
audio = AudioFileClip(random_file_path)

# decrease the volume to half
audio = audio.volumex(0.1)

# If the audio is longer than the video, trim the audio
if audio.duration > video.duration:
    audio = audio.subclip(0, video.duration)

# Set the audio of the video to the trimmed audio
video = video.set_audio(audio)

# Write the result to a file
video.write_videofile('outputwithBackgroundAudio.mp4')
