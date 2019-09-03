import os
import sys
import time
from datetime import datetime
from random import randint
import signal
import psutil
# import multiprocessing as mp


PID_FILE = "/var/run/step/demon/demon.pid"
WORK = True

def demon():

    def handler(signum, frame):
        with open("signal.log", "a") as log_file:
            log_file.write(f"Signal: {signum}\n\n")
        if signum == signal.SIGUSR2:
            frame.f_globals["WORK"] = False

    def handler_ctrl_c(signum, frame):
        with open("signal.log", "a") as log_file:
            log_file.write("Ctrl + C\n")



    signal.signal(signal.SIGUSR1, handler)
    signal.signal(signal.SIGUSR2, handler)
    signal.signal(signal.SIGINT, handler_ctrl_c)

    try:
        while WORK:
            with open("demon.log", "a") as log_file:
                log_file.write(f"{datetime.now()}\n\n")
            time.sleep(randint(5, 15))
    except Exception as e:
        with open("demon.log", "a") as log_file:
            log_file.write(f"{e}\n\n")
    finally:
        os.unlink(PID_FILE)
        return



def start_demon():
    if os.path.isfile(PID_FILE):
        with open(PID_FILE, "r") as pid_file:
            pid = int(pid_file.readline())
            for process in psutil.process_iter():
                if process.pid == pid:
                    print("Demon is working.")
                    return
    pid = os.fork()
    if pid:
        with open(PID_FILE, "w") as pid_file:
            pid_file.write(f"{pid}")
        print("Demon was started.")
        print(f"Demon has pid: {pid}")
    else:
        demon()

def get_pid():
    pid = 0
    with open(PID_FILE, "r") as pid_file:
        pid = int(pid_file.readline())
    return pid

def send_signal(arg):
    keys = {
        "-k": lambda: os.kill(get_pid(), signal.SIGKILL),
        "-c": lambda: os.kill(get_pid(), signal.SIGINT),
        "-u": lambda: os.kill(get_pid(), signal.SIGUSR1),
        "-s": lambda: os.kill(get_pid(), signal.SIGUSR2),
    }
    try:
        print(arg)
        keys[arg]()
    except KeyError as e:
        print(f"Key <{arg}> not found.")
    return




if __name__ == '__main__':
    try:
        os.mkdir(os.path.join(*os.path.split(PID_FILE)[:-1]))
    except FileNotFoundError:
        try:
            os.makedirs(os.path.join(*os.path.split(PID_FILE)[:-1]))
        except PermissionError:
            print("WTF !!!")
            sys.exit(1)
    except FileExistsError:
        pass
    args = sys.argv[1:]
    if len(args):
        send_signal(args[0])
    else:
        start_demon()

