import logging

# Konfigurerar loggningen
logging.basicConfig(
    filename='main.log',
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
    level=logging.INFO
)

import database_utils
import utils
import time

logger = logging.getLogger(__name__)

def main():
    """
    Huvudfunktionen beståendes av en evighetsloop.
    """
    print("Programmet körs...")
    logger.info('Startar')
    value = 1
    while True:
        utils.do_something(value)
        logger.info('Klar')
        time.sleep(10)

if __name__ == '__main__':
    main()