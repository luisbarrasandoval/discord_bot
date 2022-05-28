import discord
from .command import basics
from discord.ext import commands
from log import logging


DESCRIPTION = 'Mi primer bot de discord'
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', description=DESCRIPTION, intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")
    logging.info(f'Logged in as {bot.user.name}, id={bot.user.id}')


for command in dir(basics):
    if not command.startswith('__'):
        command = getattr(basics, command)
        bot.command(command.__name__)(command)
