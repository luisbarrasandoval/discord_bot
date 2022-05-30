import logging
from pathlib import Path
from datetime import datetime
import discord

DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
LOG_FOLDER = '../logs/'
NOW = datetime.now().strftime(DATE_FORMAT.replace("/", "-"))

Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)
logger = logging.getLogger('discord')

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(LOG_FOLDER + NOW + '.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

