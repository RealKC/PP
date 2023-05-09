import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from math import sqrt
from random import randint


NUMBERS: list[int] = [randint(0, 100000) for i in range(1000000)]


def is_prime(n: int) -> bool:
    n = int(n)

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False

    return True


def operation(nums: list[int]):
    nums = map(lambda n: n**2, filter(lambda n: is_prime(n), nums))
    print(nums)


def ver_1(nums: list[int]):
    threads = []
    thread_count = 2
    size = len(nums) // thread_count
    for i in range(thread_count):
        threads.append(threading.Thread(target=lambda: operation(nums[i * size:(i + 1) * size])))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def ver_2(nums: list[int]):
    operation(nums)
    operation(nums)


def ver_3(nums: list[int]):
    processes = []
    thread_count = 2
    size = len(nums) // thread_count
    for i in range(thread_count):
        processes.append(multiprocessing.Process(target=lambda: operation(nums[i * size:(i + 1) * size])))

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def ver_4(nums: list[int]):
    max_workers = 2
    size = len(nums) // max_workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(max_workers):
            future = executor.submit(lambda: operation(nums[i * size:(i + 1) * size]))


if __name__ == '__main__':
    start = time.time()
    ver_1(NUMBERS.copy())
    end = time.time()
    print("\n Timp executie pseudoparalelism cu GIL")
    print(end - start)

    start = time.time()
    ver_2(NUMBERS.copy())
    end = time.time()
    print("\n Timp executie secvential")
    print(end - start)

    start = time.time()
    ver_3(NUMBERS.copy())
    end = time.time()
    print("\n Timp executie paralela cu multiprocessing")
    print(end - start)

    start = time.time()
    ver_4(NUMBERS.copy())
    end = time.time()
    print("\n Timp executie paralela cu concurrent.futures")
    print(end - start)
