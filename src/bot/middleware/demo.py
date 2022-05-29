keywords = ['python', 'java', 'c#', 'node', 'javascript']

async def demo(bot, message):
    if any(word in message.content.lower() for word in keywords):
        await message.channel.send(f'sabes {message.author.mention}, yo tambien tengo algo de programador')
