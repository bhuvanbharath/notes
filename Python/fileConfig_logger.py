import logging
import logging.config

#call the format file
logging.config.fileConfig("logging.conf")

logger = logging.getLogger('myLogger')

logger.debug("this is debug")