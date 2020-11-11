import discord
import os

client = commands.Bot(command_prefix="p:")

client.run(os.environ['DISCORD_TOKEN'])
