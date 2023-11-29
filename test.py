from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
import numpy as np

def round_corner(radius, fill):
    """Draw a round corner"""
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=(0, 0, 0, 85))  # Set fill to fully transparent
    return corner

def round_rectangle(size, radius, fill):
    """Draw a rounded rectangle"""
    width, height = size
    rectangle = Image.new('RGBA', size, (0, 0, 0, 85))  # Use RGBA mode and fully transparent fill color
    corner = round_corner(radius, fill)
    rectangle.paste(corner, (0, 0))
    rectangle.paste(corner.rotate(90), (0, height - radius)) # Rotate the corner and paste it
    rectangle.paste(corner.rotate(180), (width - radius, height - radius))
    rectangle.paste(corner.rotate(270), (width - radius, 0))
    return rectangle

def video_quote():
    quote = "Happiness is a choice and a skill and you can dedicate yourself to learning that skill and making that choice"
    author = "Naval Ravikant"
    # Load the video clip
    video_clip = VideoFileClip("../SampleVideos/4.mp4")

    # Define the text properties
    font = "Arial-Bold"
    fontsize_quote = int(video_clip.h * 0.028)  # 5% of video height
    fontsize_author = int(video_clip.h * 0.021)  # 4% of video height
    fontsize_top = int(video_clip.h * 0.023)  # 3% of video height
    fontsize_bottom = int(video_clip.h * 0.022)  # 3% of video height

    # Set left and right margins
    left_margin = int(video_clip.w * 0.05)  # 5% of video width
    right_margin = int(video_clip.w * 0.05)  # 5% of video width

    # Define the color properties
    color_quote = 'white'
    color_author = 'white' 
    color_top = 'yellow'
    color_bottom = 'white'

    # Define the background color properties
    bgcolor_quote = (0, 0, 0)  # Black
    bgcolor_top = (255, 255, 0)  # Bright Yellow
    bgcolor_author = (0, 0, 0)  # Black
    bgcolor_bottom = (0, 0, 0)  # Black

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

    # Create the quote text clip
    quote_text_clip = TextClip(quote_text, fontsize=fontsize_quote, font=font, color=color_quote, align='center').set_duration(video_clip.duration)

    # Create rounded rectangle for the quote text clip
    quote_bg = ImageClip(np.array(round_rectangle((quote_text_clip.w + 2 * 20, quote_text_clip.h + 2 * 20), 20, bgcolor_quote)), duration=video_clip.duration)
    quote_text_clip = CompositeVideoClip([quote_bg, quote_text_clip.set_position(("center", "center"))])

    # Create the author text clip
    author_clip = TextClip(author, fontsize=fontsize_author, font=font, color=color_author).set_duration(video_clip.duration)

    # Create rounded rectangle for the author text clip
    author_bg = ImageClip(np.array(round_rectangle((author_clip.w + 2 * 20, author_clip.h + 2 * 20), 20, bgcolor_author)), duration=video_clip.duration)
    author_clip = CompositeVideoClip([author_bg, author_clip.set_position(("center", "center"))])

    # Define the top text and create the top text clip
    top_text = "Life Motivation"
    top_text_clip = TextClip(top_text, fontsize=fontsize_top, font=font, color=color_top).set_duration(video_clip.duration)

    # Create rounded rectangle for the top text clip
    top_bg = ImageClip(np.array(round_rectangle((top_text_clip.w + 2 * 20, top_text_clip.h + 2 * 20), 20, bgcolor_top)), duration=video_clip.duration)
    top_text_clip = CompositeVideoClip([top_bg, top_text_clip.set_position(("center", "center"))])

    # Define the bottom text and create the bottom text clip
    bottom_text = "dailymotivation00__"
    bottom_text_clip = TextClip(bottom_text, fontsize=fontsize_bottom, font=font, color=color_bottom).set_duration(video_clip.duration)

    # Create rounded rectangle for the bottom text clip
    bottom_bg = ImageClip(np.array(round_rectangle((bottom_text_clip.w + 2 * 20, bottom_text_clip.h + 2 * 20), 20, bgcolor_bottom)), duration=video_clip.duration)
    bottom_text_clip = CompositeVideoClip([bottom_bg, bottom_text_clip.set_position(("center", "center"))])

    # Calculate the positions for the text clips
    quote_text_position = (video_clip.w // 2 - quote_text_clip.w // 2, (video_clip.h // 2) - (quote_text_clip.h // 2))
    author_clip_position = (video_clip.w // 2 - author_clip.w // 2, quote_text_position[1] + quote_text_clip.h + int(video_clip.h * 0.02))  # 2% of video height
    top_text_position = (video_clip.w // 2 - top_text_clip.w // 2, int(video_clip.h * 0.05))  # 5% of video height
    bottom_text_position = (video_clip.w // 2 - bottom_text_clip.w // 2, video_clip.h - bottom_text_clip.h - int(video_clip.h * 0.05))  # 5% of video height

    # Set the positions for the text clips
    quote_text_clip = quote_text_clip.set_position(quote_text_position)
    author_clip = author_clip.set_position(author_clip_position)
    top_text_clip = top_text_clip.set_position(top_text_position)
    bottom_text_clip = bottom_text_clip.set_position(bottom_text_position)

    # Create a composite video clip with the quote, author, top text, and bottom text overlay
    composite_clip = CompositeVideoClip([
        video_clip,
        quote_text_clip,
        author_clip,
        top_text_clip,
        bottom_text_clip
    ])

    # Write the result to a file
    composite_clip.write_videofile("outputwithtexts.mp4")

    return "outputwithtexts.mp4"

if __name__ == "__main__":
    video_quote()

