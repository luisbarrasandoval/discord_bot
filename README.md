# Bot para Discord

### Add new command

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

### Execute

1. clone project
* `git clone https://github.com/luisbarrasandoval/discord_bot`
* `cd discord_bot`

2. install pipenv
* `pip3 install pipenv`
* `pipenv shell`

3. install dependencies
* `pipenv install`

4. change token in `src/config.py`
```python
TOKEN = 'YOUR TOKEN'
```

5. Run
* `cd src && python3 main.py`

