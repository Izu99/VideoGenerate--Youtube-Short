from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from moviepy.editor import VideoFileClip

# specify your path
path = "../SampleVideos"
save_path = "../SampleVideos"  # specify your save path

for filename in os.listdir(path):
    if filename.endswith(".mp4"):  # add more conditions if you have videos of different formats
        video_path = os.path.join(path, filename)
        clip = VideoFileClip(video_path)
        if clip.duration > 10.59:
            # If the video is longer than 10 seconds, cut it
            save_filename = os.path.join(save_path, "cut_" + filename)
            ffmpeg_extract_subclip(video_path, 0, 10, targetname=save_filename)
            # Close the VideoFileClip object
            clip.close()
            # Delete the original video
            os.remove(video_path)
            print(f"Cut and deleted {filename} as it is {clip.duration} seconds long.")
            # Rename the "cut" video back to the original name
            os.rename(save_filename, os.path.join(save_path, filename))
        else:
            # If the video is 10 seconds or less, skip it
            print(f"Skipping {filename} as it is {clip.duration} seconds long.")
            pass

