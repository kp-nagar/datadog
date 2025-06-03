import logging
import sys

# Set up logging
logger = logging.getLogger("fastapi_app")
logger.setLevel(logging.INFO)

# StreamHandler to stdout
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
