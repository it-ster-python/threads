import os
import sys
import time
from datetime import datetime
from random import randint
import signal
import psutil
# import multiprocessing as mp

PID_FILE = "/var/run/step/demon/demon.pid"


def demon():

    def handler(signum, frame):
        with open("signal.log", "a") as log_file:
            log_file.write(f"Signal: {signum}\n{frame}\n\n")

    signal.signal(signal.SIGUSR1, handler)
    signal.signal(signal.SIGUSR2, handler)
    # signal.signal(signal.SIGUSR3, handler)

    while True:
        try:
            with open("demon.log", "a") as log_file:
                log_file.write(f"{datetime.now()}\n\n")
        except KeyboardInterrupt:
            with open("signal.log", "a") as log_file:
                log_file.write("Ctrl + C")
        except Exception as e:
            pass
        finally:
            time.sleep(randint(5, 15))



def start_demon():
    if os.path.isfile(PID_FILE):
        with open(PID_FILE, "r") as pid_file:
            pid = int(pid_file.readline())
            for process in psutil.procecc_iter():
                if process.pid == pid:
                    print("Demon is working")
                    return
    pid = os.fork()
    if pid:
        with open(PID_FILE, "w") as pid_file:
            pid_file.write(f"{pid}")
        print("Demon was started")
        print(f"Demon has pid: {pid}")
    else:
        demon()

def send_signal(args):
    pass

def is_pid_file():
    return False

# def is_pid_dir():
#     return False

if __name__ == '__main__':
    try:
        os.mkdir(os.path.join(*os.path.split(PID_FILE)[:-1]))
        # arr = os.path.split(PID_FILE)
        # arr2 = arr[:-1]
        # path = os/path/join(*arr2)
        # os.mkdir(path)
    # except PermissionError:
    #     password = input("Введите пароль")
    #     command = f"mkdir {os.path.join(*os.path.split(PID_FILE)[:-1])}"
    #     os.system(f"echo {password} | sudo -S {command}")
    #     os.exit(1)
    except FileNotFoundError:
        pass
        try:
            os.makedirs(os.path.join(*os.path.split(PID_FILE)[:-1]))
        except PermissionError:
                print("WTF!!!")
                os.exit(1)
    except FileExistsError:
        pass
    args = sys.argv[1:]
    if len(args):
        send_signal(args)
    else:
        start_demon()
