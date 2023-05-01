import logging
from json_logger.log import setup_logging

setup_logging()
logger = logging.getLogger("json")

def main():
    logger.info({
        'message': 'hello',
        'context':'b'
    })

if __name__ == "__main__":
    main()
