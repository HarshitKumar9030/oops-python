import logging


logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()



file_h = logging.FileHandler('file.log')


# level and the format


stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

stream_f = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


stream_h.setFormatter(stream_f)
file_h.setFormatter(file_f)

logger.addHandler(stream_h)
logger.addHandler(file_h)