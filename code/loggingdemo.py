import logging

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.WARNING,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

# Logging messages at different levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')