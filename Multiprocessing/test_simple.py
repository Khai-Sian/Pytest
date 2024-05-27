import pytest

import sys
import logging
import multiprocessing

def init_logger():
    LOGGER = logging.getLogger()
    LOGGER.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(processName)-10s %(name)s %(levelname)-8s %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    LOGGER.addHandler(console_handler)

def log_info(msg):
    logger = logging.getLogger("IN PROCESS")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(processName)-10s %(name)s %(levelname)-8s %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info(msg)

def main():
    process = multiprocessing.Process(target=log_info, args=("HELLO",))
    logger = logging.getLogger()
    logger.info("Start Process")
    process.start()
    process.join()

if __name__ == "__main__":
    
    init_logger()
    
    main()

def test_1():
    
    init_logger()
    
    main()
