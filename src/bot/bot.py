import discord
from discord.ext import commands
from log import logging
from settings import DESCRIPTION, COMMANDS
from glob import glob
import sys

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', description=DESCRIPTION, intents=intents)

# Load all commands
for command in COMMANDS:
    sys.path.append(command)
    for file in glob(f'{command}*.py'):
        if file.endswith('__.py'):
            continue
        logging.info(f'Loading {file}')
        file = file.replace(f'{command}', '').replace('.py', '')
        module = __import__(file)
        
        bot.command(file)(getattr(module, file))
        

@bot.event
async def on_ready():
    print("Bot is ready")
    logging.info(f'Logged in as {bot.user.name}, id={bot.user.id}')

