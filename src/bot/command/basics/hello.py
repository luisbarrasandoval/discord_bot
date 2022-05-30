__AUTHOR__ = 'LFBS'
__DESCRIPTION__ = 'Saluda al usuario'
__HELP__ = __DESCRIPTION__

async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'Hello {username}!')