from PIL import Image, ImageDraw, ImageFont
import json
import mistune
import re

class ImageGen:
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

            # Add underline if requested
        # if #underline:
        #     text_width, text_height = draw.textsize(message, font=font)
        #     draw.line((message_x, message_y + text_height + 1, message_x + text_width, message_y + text_height + 1), fill="black", width=1)

        # # Add strikethrough if requested
        # if #strikethrough:
        #     text_width, text_height = draw.textsize(message, font=font)
        #     draw.line((message_x, message_y + text_height // 2, message_x + text_width, message_y + text_height // 2), fill="black", width=1)
        
        # Add the username and message text
        draw.text((140, 23), username, fill="white", font=font_reg_username)
        draw.text((140, 73), message, fill="white", font=font_reg_text)
        
        # Save or display the image
        chat_image.show()
        # chat_image.save('discord_chat.png')

    # Usage
    generate_discord_chat('KJW', './1186462663040061463.png', 'Hello, I\'m Gay! **I love mayboy!**')
    # print(text_to_list("Hello world 你1好 hrllo"))

    json_string = str(markdown('**Hello** world! _there_\n# Title\n## Title2\n> quote\n```python\nprint("Hello")\n```\n\n- list\n- list\n\n1. list\n2. list\n\n[link](https://google.com)'))
    json_string = re.sub("'", '"', json_string)
    print(json_string)
    json_data = json.loads(json_string)

    def process_json(json_data):
        for item in json_data:
            if item['type'] == 'paragraph' or item['type'] == 'list_item':
                process_json(item['children'])
            elif item['type'] == 'text':
                print(item['raw'], end='')
            elif item['type'] == 'strong':
                print('\033[1m' + item['children'][0]['raw'] + '\033[0m', end='')
            elif item['type'] == 'emphasis':
                print('\033[3m' + item['children'][0]['raw'] + '\033[0m', end='')
            elif item['type'] == 'heading':
                print('\n' + '#' * item['attrs']['level'], end='')
                process_json(item['children'])
            elif item['type'] == 'block_quote':
                print('\n>', end='')
                process_json(item['children'])
            elif item['type'] == 'block_code':
                print('\n```' + item['attrs']['info'] + '\n' + item['raw'] + '```')
            elif item['type'] == 'list':
                for child in item['children']:
                    print('\n' + ('-' if item['bullet'] == '-' else str(item['children'].index(child) + 1) + '.'), end='')
                    process_json(child['children'])
            elif item['type'] == 'link':
                print('[' + item['children'][0]['raw'] + '](' + item['attrs']['url'] + ')', end='')

    # print(process_json(json_data))