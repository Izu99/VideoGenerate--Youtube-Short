from pydub import AudioSegment

def combine_audio():
    # Open the first file
    file1 = AudioSegment.from_file("silence.wav")

    # Open the second file and resample it to match the sample rate of the first file
    file2 = AudioSegment.from_file("test-file.wav").set_frame_rate(file1.frame_rate)

    # Concatenate the two files
    output = file1 + file2

    # Export the concatenated audio to a new file
    output.export("combine_audio.wav", format="wav")

    return "combine_audio.wav"

if __name__ == "__main__":
    combine_audio()

