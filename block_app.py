import time
from threading import Thread

from datetime import datetime
import requests


def executor(url, index, results=[]):
    # file = open(f"{index}.txt", "w")
    print("start", index)
    result = requests.get(url)
    # for ind in range(1, 1000000):
        # print(f"{ind}", end="\r")
        # file.write(f"{ind}\n")
    # file.close()
    print("finish", index)
    results.append(result.text)
    return result.text


if __name__ == '__main__':

    urls = [
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by/",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by/",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by/",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by/",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by/",
    ]

    # start = datetime.now()
    # results = map(executor, urls, range(len(urls)))
    # for element in results:
    #     pass
    # finish = datetime.now()
    # print(finish - start)

    results = []
    start = datetime.now()
    workers = [Thread(target=executor, args=(urls[index], index, results)) for index in range(len(urls))]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    finish = datetime.now()
    print(finish - start)
    print(len(results))
    
    # results = []
    # start = datetime.now()
    # for index in range(len(urls)):
    #     results.append(executor(urls[index], index))
    # finish = datetime.now()
    # print(finish - start)
    # print(len(results))
