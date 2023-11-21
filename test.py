import os
from moviepy.editor import AudioFileClip

# specify the path to the mp3 file
audio_file_path = '../SampleAudios/10.mp3'

# pass the mp3 file to AudioFileClip
audio = AudioFileClip(audio_file_path)

# decrease the volume to half
audionew = audio.volumex(0.1)

# Write the result to a file
output_file_path = 'half_volume_101.mp3'
audionew.write_audiofile(output_file_path)
