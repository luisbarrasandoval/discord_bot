__AUTHOR__ = 'LFBS'
__DESCRIPTION__ = 'suma los numeros'
__HELP__ = "args: list<numbers>"

async def add(ctx, *args):
    if len(args) == 0:
        await ctx.send(f'{ctx.author.mention} You need to specify a number to add.')
        return
    try:
        result = sum(map(int, args))
        await ctx.send(f'{ctx.author.mention} The result is {result}')
    except ValueError:
        await ctx.send(f'{ctx.author.mention} You need to specify a number to add.')