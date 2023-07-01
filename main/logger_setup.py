import logging

def setup_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(name)s, %(message)s')

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
