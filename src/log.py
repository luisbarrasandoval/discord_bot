import logging
from pathlib import Path
from datetime import datetime

DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
LOG_FOLDER = '../logs/'
NOW = datetime.now().strftime(DATE_FORMAT.replace("/", "-"))

Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FOLDER + NOW + '.log',
    encoding='utf-8',
    level=logging.INFO,
    format='%(levelname)s - %(asctime)s - %(message)s',
    datefmt=DATE_FORMAT)

