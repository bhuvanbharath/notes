# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%d/%m/%y %H:%M:%S')

# import helper

# logging.debug("this is debug level")
# logging.info("this is info level")
# logging.warning("this is warning level")
# logging.error("this is error level")
# logging.critical("this is critical level")


#----- HANDLERS -----
#CREATING HANDLERS
import logging 
logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("logFile.log")

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is warning")
logger.error("this is error")