from random import randint
from threading import Thread, Condition
from queue import Queue, Empty


class Consumer(Thread):
    def __init__(self, mq: Queue):
        super().__init__()
        self.queue = mq

    def run(self):
        i = 0
        try:
            while True:
                message = self.queue.get(timeout=0.5)
                i = i + 1
                print(f'[iteratia #{i}] Am primit si utilizat elementul: {message}')
                print(f'Mai asteptam')
                self.queue.task_done()
        except (ValueError, Empty):
            print(f'Done processing, we received a total of {i} messages')
            pass


class Producer(Thread):
    def __init__(self, mq: Queue):
        super().__init__()
        self.queue = mq

    def run(self):
        for i in range(30):
            self.queue.put(randint(0, 1000))
        self.queue.join()


if __name__ == '__main__':
    mq = Queue()
    producer = Producer(mq)
    consumer = Consumer(mq)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
