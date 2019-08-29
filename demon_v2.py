import os
import sys
import time
from datetime import datetime
from random import randint
import signal


PID_FILE = "/var/run/demon/demon.pid"


def demon():

    def handler(signum, frame):
        with open("signal.log", "a") as log_file:
            log_file.write(f"Signal: {signum}\n{frame}\n\n")

    signal.signal(signal.SIGUSR1, handler)
    signal.signal(signal.SIGUSR2, handler)
    signal.signal(signal.SIGUSR3, handler)

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
    pid = demon()


def send_signal(args):
    pass

def is_pid_file():
    return False

# def is_pid_dir():
#     return False

if __name__ == '__main__':
    try:
        try:
            os.mkdir(os.path.join(*os.path.split(PID_FILE)[:-1]))
            # arr = os.path.split(PID_FILE)
            # arr2 = arr[:-1]
            # path = os/path/join(*arr2)
            # os.mkdir(path)
        except PermissionError:
            pass
        except FileNotFoundError:
            try:
                makedirs(os.path.join(*os.path.split(PID_FILE)[:-1]))
                except PermissionError:
                    print("WTF!!!")
                    os.exit(1)
    except os.FileExistsError:
        pass
    try:
        args = sys.argv[1:]
    except IndexError:
        start_demon()
    else:
        send_signal(args)
