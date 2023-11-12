import addMusicToTheVideo
import getQuotes
import addQuote
import convertQuoteToSpeech
import combineAudio
import addSpeechToVideo
import deleteFiles
from IPython.display import Video
import time
# import automateUtube

# Record the start time
start_time = time.time()

print("Program Start", flush=True)

print("****** Adding background Music To the Video ******")
video_music = (
    addMusicToTheVideo.get_random_video()
)  # call the background music function
print("****** Background Music Added ******")

print("****** Getting Quote and Author From the API ******")
quote, author = "\"The greatest glory in living lies not in never falling. but in rising every time we fall.\"", "- Nelson Mandela"  # get quote and author

print(f"{quote} - {author}")

print("****** Adding Quote To the video ******")
quote_video = addQuote.video_quote(quote, author)  # add values to video_quote parameters

print("****** Quote Added Successfully ******")

print("****** Convert Quote To Voice ******")
voice = convertQuoteToSpeech.text_to_speech(quote)  # Call the function with the text from this file
print(voice)
print("****** Voice Is Successfully Created ******")

combine_audio = combineAudio.combine_audio()
print(combine_audio)

print("****** adding Voice To the Video ******")
final_video = addSpeechToVideo.text_to_video(quote_video, combine_audio)
print("****** Voice Added Successfully ******")

# Display and play the video
Video(final_video)

# print("****** File Is Uploading ******")
# author = author.replace("-","")
# video_title = automateUtube.main(author)
# print(author)

print("****** Deleting Files ******")
deleteFiles.delete_file()
print("****** Files Deleted Successfully ******")

# Record the end time
end_time = time.time()

# Calculate the total runtime
total_runtime = end_time - start_time

# Print the total runtime in seconds
print(f"Total runtime: {total_runtime:.2f} seconds")

