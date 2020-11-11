import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="p:")
client.remove_command('help')

client.run(os.environ['DISCORD_TOKEN'])

