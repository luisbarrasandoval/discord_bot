__AUTHOR__ = 'LFBS'
__DESCRIPTION__ = 'Calculadora simple'

import re
REGEX = '([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)'

async def calculator(bot, message):
    content = message.content.lower().replace(' ', '')
    if re.search(REGEX, content):
        await message.channel.send(f'{eval(message.content)}')