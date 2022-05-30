__AUTHOR__ = 'LFBS'
__DESCRIPTION__ = 'Muestra dependiendo del mensaje que se le pase'


keywords = ['python', 'java', 'c#', 'node', 'javascript']
async def demo(bot, message):
    m = message.content.lower()
    if "oferta" in m and  any(word in m for word in keywords):
        await message.channel.send(f'{message.author.mention} a publicado una oferta de trabajo')
