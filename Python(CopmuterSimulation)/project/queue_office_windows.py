import multiprocessing
import random

import requests

queue = multiprocessing.Queue(maxsize=800)
queue_not_match = multiprocessing.Queue()

class Petitioner:
    def __init__(self, case):
        self.case = case


def go_to_window(petitioner):
    post = requests.post("http://127.0.0.1:5000/petitioner/add/" + str(petitioner.case))
    if str(post.status_code) == str(404):
        queue_not_match.put(petitioner)


def add_petitioner_to_queue(queue, queue_not_match):
    print(queue.qsize())
    while not queue.empty():
        if queue_not_match.empty():
            petitioner = queue.get()
        else:
            petitioner = queue_not_match.get()
        go_to_window(petitioner)
        print("Queue size: " + str(queue.qsize()))


def is_any_window_busy():
    response = requests.get("http://127.0.0.1:5000/window/busy")
    if response.status_code == 404:
        return True
    return False


def remove_petitioner_from_window():
    while is_any_window_busy() or not queue.empty():
        requests.post("http://127.0.0.1:5000/window/" + str(random.randint(1, 3)))




if __name__ == '__main__':
    case_1 = 1  # A, B, C
    case_2 = 2  # C, D

    # queue = multiprocessing.Queue(maxsize=800)
    # queue_not_match = multiprocessing.Queue()
    for i in range(random.randint(100, 900)):
        try:
            queue.put(Petitioner(random.randint(1, 2)))
        except Exception:
            print("Queue is full you can come back later")

    processes = []
    print(queue.qsize())


    add_to_queue = multiprocessing.Process(target=add_petitioner_to_queue,
                                           args=[queue, queue_not_match, ],
                                           name="add_to_window")
    remove_from_queue = multiprocessing.Process(target=remove_petitioner_from_window,
                                                name="remove_from_window")
    add_to_queue.start()
    # add_to_queue.join()
    processes.append(add_to_queue)
    remove_from_queue.start()
    # remove_from_queue.join()
    processes.append(remove_from_queue)