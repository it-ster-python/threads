import multiprocessing as mp
import threading as th
import time


def executor(index, res=[]):
    print("Executor start", index)
    time.sleep(5)
    res.append(index)
    print("Executor finish", index)


def thread():
    result = []
    worker1 = th.Thread(target=executor, args=(1, result))
    worker2 = th.Thread(target=executor, args=(2, result))

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()
    print(result)


def proc():
    result = []
    worker1 = mp.Process(target=executor, args=(1, result))
    worker2 = mp.Process(target=executor, args=(2, result))

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()
    print(result)


if __name__ == '__main__':
    print("proc start")
    proc()

    print("thread start")
    thread()