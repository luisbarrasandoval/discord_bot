import sys
import discord
from discord.ext import commands, tasks
from log import logger
from settings import DESCRIPTION, COMMANDS, MIDDLEWARES, COMMAND_PREFIX
from glob import glob


class Bot(commands.Bot):

    commands = {}
    middlewares = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._load_commands()
        self._loads_middlewares()
    

    async def on_ready(self):
        print("Bot is ready")
        logger.info(f'Logged in as {bot.user.name}, id={bot.user.id}')


    async def help_command(self):
        return super().help_command(
            command_attrs={
                'name': 'help',
                'aliases': ['ayuda', 'h'],
                'help': 'Muestra la ayuda de un comando',
                'usage': '<comando>'
            }
        )
    

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            command = ctx.message.content.split()[0][1:]


            if command[-1] == '?' and command[:-1] in self.commands.keys():
                embed = discord.Embed(
                    title=f'{command[:-1]}',
                    description=self.commands[command[:-1]]['description'],
                    color=discord.Color.blue()
                )

                embed.set_footer(text=self.commands[command[:-1]]['help'])
                await ctx.send(embed=embed)
                return

            list_commands = '\n'.join(self.commands.keys())
            embed = discord.Embed(
                title=f'`!{command}` no es un comando valido',
                color=0x00ff00,
                description="Este es un listado de comandos disponibles:\n"
            )

            for command in self.commands:
                embed.add_field(
                    name=f'{COMMAND_PREFIX}{command}',
                    value=self.commands[command]['help'],
                    inline=False
                )

            await ctx.send(embed=embed)

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
        for middleware in self.get_dynamic_modules(MIDDLEWARES):
            module = __import__(f'{middleware}')
            self.middlewares.append(getattr(module, middleware))
            logger.info(f'Loaded middleware {middleware}')

    def _load_commands(self):
        for command in self.get_dynamic_modules(COMMANDS):
            module = __import__(f'{command}')
            self._load_command(module, command)

            self.commands[command] = {
                'help': module.__HELP__,
                'description': module.__DESCRIPTION__,
            }


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
bot = Bot(command_prefix=COMMAND_PREFIX, description=DESCRIPTION, intents=intents)
