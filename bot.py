import discord
from classes.imagegen import ImageGen

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/q'):
        if message.content == "/q":
            q = 1
        else:
            q = int(message.content.split(" ")[1])
        ImageGen.generate_discord_chat()

client.run("")