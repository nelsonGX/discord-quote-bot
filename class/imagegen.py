
from PIL import Image, ImageDraw, ImageFont
import mistune

markdown = mistune.create_markdown(renderer='ast')

def generate_discord_chat(username, avatar_path, message):
    # Load the avatar image
    avatar = Image.open(avatar_path).resize((100, 100))

    mask = Image.new('L', (100, 100), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 100, 100), fill=255)
    
    # Apply the mask to the avatar
    avatar.putalpha(mask)
    
    # Create a new image with white background
    chat_image = Image.new('RGB', (700, 150), '#1C1D22')
    draw = ImageDraw.Draw(chat_image)
    
    # Place the avatar on the left
    chat_image.paste(avatar, (10, 25), mask=avatar)
    
    # Load a font
    font_reg_username = ImageFont.truetype("fonts/ggsans-mid.ttf", 36)
    font_reg_text = ImageFont.truetype("fonts/ggsans-reg.ttf", 40)
    font_bold_text = ImageFont.truetype("fonts/ggsans-semibold.ttf", 40)
    font_title_text = ImageFont.truetype("fonts/ggsans-bold.ttf", 40)
    font_chinese_text = ImageFont.truetype("fonts/微軟正黑體-1.ttf", 40)
    
    # Add the username and message text
    draw.text((140, 23), username, fill="white", font=font_reg_username)
    draw.text((140, 73), message, fill="white", font=font_reg_text)
    
    # Save or display the image
    chat_image.show()
    # chat_image.save('discord_chat.png')

# Usage
# generate_discord_chat('KJW', './1186462663040061463.png', 'Hello, I\'m Gay! **I love mayboy!**')
# print(text_to_list("Hello world 你1好 hrllo"))
print(markdown("Hello **world** 你1好 hrllo"))