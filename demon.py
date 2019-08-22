import sys
import os
import time
import signal


def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGUSR1, handler)


def demon():
    sys.stdin.close()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Работаем дальше")
        pass

try:
    if sys.argv[1] == "-k":
        with open("demon.pid", "r") as pid_file:
            os.kill(int(pid_file.read()), signal.SIGKILL)
            os.unlink("demon.pid")
    elif sys.argv[1] == "-c":
        with open("demon.pid", "r") as pid_file:
            os.kill(int(pid_file.read()), signal.SIGINT)
    elif sys.argv[1] == "-u":
        with open("demon.pid", "r") as pid_file:
            os.kill(int(pid_file.read()), signal.SIGUSR1)
except IndexError:
    pid = os.fork()
    if pid == 0:
        demon()
    else:
        if not os.path.isfile("demon.pid"):
            with open("demon.pid", "w") as pid_file:
                pid_file.write(f"{pid}")
            print("Master close")
            print("Demon has pid {}".format(pid))
        else:
            print("Демон уже запущен!!!")



    # time.sleep(10)
    # os.kill(pid, signal.SIGKILL)
