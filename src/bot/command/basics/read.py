import discord
from gtts import gTTS

__AUTHOR__ = 'LFBS'
__DESCRIPTION__ = 'Lee un texto y lo envia como audio'
__HELP__ = __DESCRIPTION__

async def read(ctx):
    text = ctx.message.content.split()[1:]
    text = ' '.join(text)
    tts = gTTS(text=text, lang='es')
    tts.save('read.mp3')
    
    await ctx.send(file=discord.File('read.mp3'))