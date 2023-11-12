from moviepy.editor import AudioFileClip
import os

# specify your path
path = "../SampleAudios"

count = 1

for filename in os.listdir(path):
    if filename.endswith(".mp3"):  # add more conditions if you have audios of different formats
        audio_path = os.path.join(path, filename)
        audio = AudioFileClip(audio_path)
        duration = audio.duration

        # Only process audio files longer than 16 seconds
        if duration > 16:
            start_time = 0
            end_time = 15
           

            while start_time < duration:
                # If the end time exceeds the duration of the audio, set it to the duration
                end_time = min(end_time, duration)
                # Extract part of the audio file
                part_audio = audio.subclip(start_time, end_time)
                # If the part is less than 15 seconds, break the loop
                if part_audio.duration < 15:
                    break
                # Save part to disk
                part_audio.write_audiofile(os.path.join(path, f"{count}.mp3"))
                # Move to next part
                start_time += 15
                end_time += 15
                count += 1

            # Close the original audio file
            audio.close()
            # Delete the original audio file
            os.remove(audio_path)