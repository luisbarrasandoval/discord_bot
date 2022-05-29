# Bot for Discord

### Add new command

Each command is a .py file that will be loaded dynamically when the bot starts. the command function must have the same file name.
<br>
Example: `hello.py`
```python
# simple command example
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'Hello {username}!')
```

The `setting.py` file defines the list of `COMMAND` directories, the bot will look for commands in those folders
```python
DESCRIPTION = 'Mi primer bot de discord'
COMMANDS = ['bot/command/basics/']
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

