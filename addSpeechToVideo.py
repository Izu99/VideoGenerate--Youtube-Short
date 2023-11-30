from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from datetime import datetime
from shutil import copyfile


def text_to_video(quote_video, voice):
    # Get the current date as a string in the format YYYY-MM-DD
    current_date = datetime.now().date().strftime("%Y-%m-%d")

    # Get the current time as a string in the format HH:MM:SS
    current_time = datetime.now().strftime("%H:%M:%S")

    # load the video clip
    videoclip = VideoFileClip(quote_video)

    # load the audio clip
    audioclip = AudioFileClip(voice)

    # get the original audio of the video clip
    original_audio = videoclip.audio

    # create a composite audio clip with the original audio and the new audio
    composite_audio = CompositeAudioClip([original_audio, audioclip])

    # set the audio of the video clip to the composite audio clip
    videoclip = videoclip.set_audio(composite_audio)

    # Concatenate the date and the time strings with an underscore
    file_name = f"{current_date}_{current_time.replace(':', '_')}.mp4"

    # Add the relative path of the folder to the file name
    file_name = f"../ShortVideos/{file_name}"

    # Write the video clip to the file
    videoclip.write_videofile(file_name)

    # Copy the video file to the current path with the name "final_video.mp4"
    copyfile(file_name, "final_video.mp4")

    return file_name


if __name__ == "__main__":
    text_to_video()
