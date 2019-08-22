import multiprocessing as mp
import threading as th
import time


def executor(index, queue):
    print("Executor start", index)
    time.sleep(5)
    queue.put(index)
    print("Executor finish", index)


def proc():
    q = mp.Queue()
    worker1 = mp.Process(target=executor, args=(1, q))
    worker2 = mp.Process(target=executor, args=(2, q))

    worker1.start()
    worker2.start()

    print(q.get())
    print(q.get())

    worker1.join()
    worker2.join()


if __name__ == '__main__':
    print("proc start")
    proc()
