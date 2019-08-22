from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

from datetime import datetime
import requests


def executor(url):
    file = open(f"{url.split('//')[-1]}.txt", "w")
    print("start", url)
    # result = requests.get(url)
    for ind in range(1, 100000):
        print(f"{ind}", end="\r")
        file.write(f"{ind}\n")
    file.close()
    print("finish", url)
    return result.text

urls = [
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by",
        "https://google.com",
        "https://hh.ru",
        "https://yandex.ru",
        "http://www.pogoda.by",
    ]

if __name__ == '__main__':

    pool = ThreadPool(len(urls))

    start = datetime.now()
    results = pool.map(executor, urls)

    print(len(results))
    finish = datetime.now()
    pool.close()
    pool.join()
    print(finish - start)
