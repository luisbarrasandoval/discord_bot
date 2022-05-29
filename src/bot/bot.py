import sys
import discord
from discord.ext import commands, tasks
from log import logger
from settings import DESCRIPTION, COMMANDS, MIDDLEWARE
from glob import glob


class Bot(commands.Bot):

    middlewares = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._load_commands()
        self._loads_middlewares()

    async def on_ready(self):
        print("Bot is ready")
        logger.info(f'Logged in as {bot.user.name}, id={bot.user.id}')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            command = ctx.message.content.split()[0][1:]
            list_commands = '\n'.join(
                f'`{command}`' for command in self.get_dynamic_modules(COMMANDS))
            await ctx.send(f'Command `{command}` not found.\nAvailable commands:\n{list_commands}')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Missing required argument: {error.param.name}')

        else:
            logger.error(f'{error}')
            await ctx.send(f'{error}')

    async def on_message(self, message):
        if message.author.bot:
            return

        for middleware in self.middlewares:
            try:
                await middleware(self, message)
            except Exception as e:
                logger.error(f'{e}')
                return

        await self.process_commands(message)

    def _loads_middlewares(self):
        for middleware in self.get_dynamic_modules(MIDDLEWARE):
            module = __import__(f'{middleware}')
            self.middlewares.append(getattr(module, middleware))
            logger.info(f'Loaded middleware {middleware}')

    def _load_commands(self):
        for command in self.get_dynamic_modules(COMMANDS):
            module = __import__(f'{command}')
            self._load_command(module, command)

    def _load_command(self, module, file):
        try:
            self.command(file)(getattr(module, file))
            logger.info(f'Loaded command {file}')
        except AttributeError:
            logger.error(f'{file} has no function')

    def get_dynamic_modules(self, path: list):
        commands = []

        for command in path:
            sys.path.append(command)
            for file in glob(f'{command}*.py'):
                if file.endswith('__.py'):
                    continue
                file = file.replace(f'{command}', '').replace('.py', '')
                commands.append(file)

        return commands


intents = discord.Intents.default()
bot = Bot(command_prefix='!', description=DESCRIPTION, intents=intents)
