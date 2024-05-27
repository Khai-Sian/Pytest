import pytest

import random
import logging
from multiprocessing import *

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

stdout_lock = Lock()

class obj():
    def __init__(self, data):
        self._intro = ("This is data: %s\n" % data)

def simple_1(data):
    
    entry = obj(data)
    logger = logging.getLogger(__name__)
    logger.info(f"Creating object for {data}")

def simple_2(data_list):

    with stdout_lock:
        data = data_list[0]
        messages_list = data_list[1]
        log_dict = data_list[2]
        
    entry = obj(data)
    
    with stdout_lock:
        messages_list.append(entry._intro)
        log_dict[20].append(f"Creating Object for {data}")

    return entry

def test_1():
    #data = ["Dog", "Cat", "Fox", "Fish", "Rabbit", "Turtle"]
    data = random.sample(range(1, 1000), 500)

    cpus_to_use = min(4, cpu_count() - 1)
    pool = Pool(cpus_to_use)

    manager = Manager()
    messages_list = manager.list()

    data_list = [[entry, messages_list] for entry in data] 

    LOGGER.critical("Start Multiprocessing")
    # answer = pool.map(simple, data_list)
    # pool.close()
    # pool.join()
 
    proc1 = Process(target = simple_1, args = (20,))
    proc2 = Process(target = simple_1, args = (50,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

def test_2():
    #data = ["Dog", "Cat", "Fox", "Fish", "Rabbit", "Turtle"]
    data = random.sample(range(1, 1000), 10)

    cpus_to_use = min(4, cpu_count() - 1)
    pool = Pool(cpus_to_use)

    manager = Manager()
    messages_list = manager.list()

    log_dict = manager.dict()
    log_dict[10] = manager.list()
    log_dict[20] = manager.list()
    log_dict[30] = manager.list()

    data_list = [[entry, messages_list, log_dict] for entry in data] 

    LOGGER.critical("Start Multiprocessing")
    answer = pool.map(simple_2, data_list)
    pool.close()
    pool.join()

    for message in messages_list:
        LOGGER.critical(message)

    for log_level, messages in log_dict.items():

        # print("Log Level: ", log_level)
        # print(messages)

        if log_level == 10:
            for message in messages:
                LOGGER.debug(message)
        elif log_level == 20:
            for message in messages:
                LOGGER.info(message)
        elif log_level == 30:
            for message in messages:
                LOGGER.critical(message)

if __name__ == "__main__":

    test_1()
    test_2()