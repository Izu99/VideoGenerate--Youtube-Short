import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip

def get_random_video():
    video_folder = '../SampleVideos'  # The path to your video folder
    videos = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]
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

# Load your audio
audio = AudioFileClip('../SampleAudio/price-of-freedom-33106.mp3')

# If the audio is longer than the video, trim the audio
if audio.duration > video.duration:
    audio = audio.subclip(0, video.duration)

# Set the audio of the video to the trimmed audio
video = video.set_audio(audio)

# Write the result to a file
video.write_videofile('outputwithBackgroundAudio.mp4')

