async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'Hello {username}!')