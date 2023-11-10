from ast import main
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def text_to_video(quote_video, voice):
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

    # save the result
    videoclip.write_videofile("final_video.mp4")

    return "final_video.mp4"

if __name__ == "__main__":
    text_to_video()
