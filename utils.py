import logging
import time
from database_utils import create_table, create

logger = logging.getLogger(__name__)

def do_something(value):
    logger.info('Gör någonting')
    name = "Observation"
    create(name, value)
    logger.info(f"Observation tillagd i databasen.")

create_table()