import discord
import os

client = discord.client()

@client.event
async def on_ready():
       print("bot is ready!")
client.run(os.environ['Discord_Token'])
