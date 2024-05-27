from gc import isenabled
import logging
import logging.handlers
import multiprocessing
from time import sleep
from random import random, randint

LOGGER  = logging.getLogger()

INFO = False

import pytest

# @pytest.fixture(scope = 'module')
# def global_data():
#     return {"INFO": False}

def test_test():

    global INFO

    if LOGGER.isEnabledFor(logging.INFO):
        # global_data["INFO"] = True
        INFO = True
    else:
        # global_data["INFO"] = False
        INFO = False

    # print("LOGGER INFO is set to: ", global_data["INFO"])
    # print(type(global_data["INFO"]))

    # print("LOGGER INFO is set to: ", pytest.INFO)
    # print(type(pytest.INFO))

    # INFO = pytest.INFO
    print("Global INFO is set to: ", INFO)

    main()

# Almost the same as the demo code, but added `console_handler` to directly
# read logging info from the console
def listener_configurer(INFO):
    root = logging.getLogger()
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

    # print("Listener configurer: ", INFO)
    # print("is TRUE") if INFO else print("is False")
    root.setLevel(logging.INFO) if INFO else root.setLevel(logging.CRITICAL)


# Almost the same as the demo code, but made it into a forever loop. This is
# more likely to happen in an app that does not have a clear end point, e.g.
# a deployed IoT sensor. Another change is to show that if configurer is not
# passed but directly visible by the process function, calling it directly has
# the same effect.
def listener_process(queue, status, INFO):
    listener_configurer(INFO)
    total = 0
    while True:
        while not queue.empty():
            record = queue.get()
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        sleep(1)

        if status.get() == "FINISHED":
            return

        # while not status.empty():
        #     total = total + int(status.get())
        #     print("Total: ", total)
        #     if total == 3:
        #         return


# Same as demo code
def worker_configurer(queue, INFO):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    # root.setLevel(logging.DEBUG)
    root.setLevel(logging.INFO) if INFO else root.setLevel(logging.CRITICAL)


# Almost the same as demo code, except the logging is simplified, and configurer
# is no longer passed as argument.
def worker_process(queue, status, INFO):
    worker_configurer(queue, INFO)
    for i in range(10):
        # sleep(random())
        sleep(0.2)
        innerlogger = logging.getLogger('worker')
        innerlogger.info(f'Logging a random number {randint(0, 10)}')
        # print(f'Logging a random number {randint(0, 10)}')
    status.put(1)



def main():

    print("Before everything: ", INFO)

    queue = multiprocessing.Queue(-1)
    status = multiprocessing.Queue()
    listener = multiprocessing.Process(
        target=listener_process, args=(queue, status, INFO))
    listener.start()
    workers = []
    for i in range(10):
        worker = multiprocessing.Process(target=worker_process, args=(queue, status, INFO))
        workers.append(worker)
        worker.start()
    for w in workers:
        w.join()

    status.put("FINISHED")
    listener.join()

if __name__ == '__main__':
    main()

# import sys

# def master_process(queue, LOGGER):
# def master_process(queue):
    
#     LOGGER = logging.getLogger()
#     console_handler = logging.StreamHandler(sys.stdout)
#     LOGGER.addHandler(console_handler)
#     LOGGER.setLevel(logging.INFO)
    
    # while True:
    #     while not queue.empty():
    #         record = queue.get()
    #         if record != "FINISHED":
    #             LOGGER.info(record)
    #             # print(record)
    #         else:
    #             return
    #     sleep(1)

    # LOGGER.info("HELLO")
    # print("HELLO")

# def worker_process(data_list):
# def worker_process(queue):

#     # queue = data_list[1]

#     for i in range(3):
#         sleep(random())
#         queue.put(f'Logging a random number {randint(0, 10)}')
#         # print(f'Logging a random number {randint(0, 10)}')

# def main2():

#     LOGGER = logging.getLogger()
#     LOGGER.setLevel(logging.DEBUG)

#     queue = multiprocessing.Queue(-1)

#     # listener = multiprocessing.Process(
#     #     target=master_process, args=(queue,))
#     # listener.start()

#     LOGGER.info("START WORKER PROCESS")
#     workers = []
#     for i in range(3):
#         worker = multiprocessing.Process(target=worker_process, args=(queue,))
#         workers.append(worker)
#         worker.start()

#     # for w in workers:
#     #     w.join()

#     for w in workers:
#         while w.is_alive():
#             while not queue.empty():
#                 record = queue.get()
#                 # print(record)
#                 LOGGER.info(record)
#         w.join()

    # queue.put("FINISHED")
    # listener.join()







    # manager = multiprocessing.Manager()
    # queue = manager.Queue()

    # LOGGER.critical("Start listener process")
    # listener = multiprocessing.Process(target=master_process, args=(queue, LOGGER))
    # listener.start()

    # pool = multiprocessing.Pool(4)

    # values = [[i, queue] for i in range(5)]

    # pool.map(worker_process, values)

    # # while pool._state == "RUN":
    # while not queue.empty() or queue.get() != "FINISHED":
    #     record = queue.get()
    #     LOGGER.info(record)

    # pool.close()
    # pool.join()

    # queue.put("FINISHED")

    # listener.join()

    

# if __name__ == '__main__':
#     main2()

# import pytest

# def test_test():
#     main2()

