# import logging

# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=10)
# logger.addHandler(handler)

# [logger.info("this is info") for _ in range(100000)]


#--- TimeRotatingFileHandler ---
from cgitb import handler
import logging 
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler('app.log', when ='s', interval=2, backupCount=5)

logger.addHandler(handler)
for _ in range(5):
    logger.info("this is info")
    logger.info("this is info2")
    time.sleep(5)