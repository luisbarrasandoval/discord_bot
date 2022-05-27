# Bot para Discord

Edit <a href='src/bot/command/basics.py'>`src/bot/command/basics.py`</a> to add new simple commands (no arguments). They will be loaded automatically when you start the bot
```python
# simple command example
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'Hello {username}!')

async def new_command(ctx):
    await ctx.send(f'response new command')

...
```

### Start

clone project
* `git clone https://github.com/luisbarrasandoval/discord_bot`
* `cd discord_bot`

install pipenv
* `pip3 install pipenv`
* `pipenv shell`

install dependencies
* `pipenv install`

Run
* `cd src && python3 main.py`

