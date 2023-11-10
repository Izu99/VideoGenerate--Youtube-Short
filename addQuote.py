from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def video_quote(quote, author):
    # Load the video clip
    video_clip = VideoFileClip("outputwithbackgroundAudio.mp4")

    # Define the text properties
    font = "Arial-Bold"
    fontsize_quote = 55
    fontsize_author = 38
    fontsize_top = 40
    fontsize_bottom = 40
    
    # Define the background color properties
    bgcolor_quote = (0, 0, 0)  # Black
    bgcolor_top = (255, 255, 0)  # Yellow

    # Set left and right margins
    left_margin = 60
    right_margin = 60

    # Calculate the available width for the quote text
    quote_width = video_clip.w - (left_margin + right_margin)

 # Define the quote and create the quote text clip
    lines = []
    current_line = ""
    words = quote.split(" ")
    for word in words:
        line = current_line + word + " "
        if TextClip(line, fontsize=fontsize_quote, font=font).w > quote_width:
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line = line
    lines.append(current_line.strip())
    quote_text = "\n".join(lines)
    quote_text_clip = TextClip(quote_text, fontsize=fontsize_quote, font=font, color='white', align='center')
    quote_text_clip = quote_text_clip.on_color(size=(quote_text_clip.w + 2 * 20, quote_text_clip.h + 2 * 20), color=bgcolor_quote, col_opacity=0.4)

    # Define the author and create the author text clip
    author_clip = TextClip(author, fontsize=fontsize_author, font=font, color='white')
    author_clip = author_clip.on_color(size=(author_clip.w + 2 * 20, author_clip.h + 2 * 20), color=bgcolor_quote, col_opacity=0.4)

    # Define the top text and create the top text clip
    top_text = "Life Motivation"
    top_text_clip = TextClip(top_text, fontsize=fontsize_top, font=font, color='black')
    top_text_clip = top_text_clip.on_color(size=(top_text_clip.w + 2 * 20, top_text_clip.h + 2 * 20), color=bgcolor_top, col_opacity=0.7)

    # Define the bottom text and create the bottom text clip
    bottom_text = "dailymotivation00__"
    bottom_text_clip = TextClip(bottom_text, fontsize=fontsize_bottom, font=font, color='white')
    bottom_text_clip = bottom_text_clip.on_color(size=(bottom_text_clip.w + 2 * 20, bottom_text_clip.h + 2 * 20), color=bgcolor_quote, col_opacity=0.4)

    # Calculate the positions for the text clips
    quote_text_position = (video_clip.w // 2 - quote_text_clip.w // 2, (video_clip.h // 2) - (quote_text_clip.h // 2))
    author_clip_position = (video_clip.w // 2 - author_clip.w // 2, quote_text_position[1] + quote_text_clip.h + 20)
    top_text_position = (video_clip.w // 2 - top_text_clip.w // 2, 50)
    bottom_text_position = (video_clip.w // 2 - bottom_text_clip.w // 2, video_clip.h - bottom_text_clip.h - 20)

    # Set the positions for the text clips
    quote_text_clip = quote_text_clip.set_position(quote_text_position)
    author_clip = author_clip.set_position(author_clip_position)
    top_text_clip = top_text_clip.set_position(top_text_position)
    bottom_text_clip = bottom_text_clip.set_position(bottom_text_position)

    # Create a composite video clip with the quote, author, top text, and bottom text overlay
    composite_clip = CompositeVideoClip([
        video_clip,
        quote_text_clip.set_duration(video_clip.duration),
        author_clip.set_duration(video_clip.duration),
        top_text_clip.set_duration(video_clip.duration),
        bottom_text_clip.set_duration(video_clip.duration)
    ])

    # Write the result to a file
    composite_clip.write_videofile("outputwithtexts.mp4")

    return "outputwithtexts.mp4"

if __name__ == "__main__":
    video_quote()