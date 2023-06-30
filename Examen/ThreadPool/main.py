from enum import Enum
from queue import Queue
import threading as thr
from abc import ABC, abstractmethod


class ThreadCommand(ABC):
    @abstractmethod
    def execute(self, thread):
        raise NotImplementedError(f'ThreadCommand: abstract method `execute` not implemented by {self.__class__.__name__}')


class ThreadState(Enum):
    RUN_TASKS = 0
    PAUSED = 1
    STOPPED = 2
    STOP_ON_NO_TASKS = 3


class Thread(thr.Thread):
    queue: Queue = Queue()
    _state: ThreadState = ThreadState.PAUSED
    lock: thr.RLock = thr.RLock()

    def __init__(self, tid):
        super().__init__()

        self.id = tid
        self.tasks = []

    def set_state(self, new_state: ThreadState):
        with self.lock:
            self._state = new_state

    def get_state(self) -> ThreadState:
        with self.lock:
            return self._state

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)

    def run(self):
        while True:
            cmd = self.queue.get()
            cmd.execute(self)

            with self.lock:
                match self._state:
                    case ThreadState.RUN_TASKS:
                        if len(self.tasks) == 0:
                            continue
                        self.tasks.pop()()
                    case ThreadState.PAUSED:
                        pass
                    case ThreadState.STOPPED:
                        return
                    case ThreadState.STOP_ON_NO_TASKS:
                        if len(self.tasks) == 0:
                            return
                        self.tasks.pop()()


class AddTaskToThread(ThreadCommand):
    def __init__(self, task):
        self.task = task

    def execute(self, thread):
        thread.add_task(self.task)


class InspectThread(ThreadCommand):
    def execute(self, thread):
        print(f'thread-{thread.id}: state: {thread.get_state()}')


class PauseThread(ThreadCommand):
    def execute(self, thread):
        thread.set_state(ThreadState.PAUSED)


class StopThread(ThreadCommand):
    stop_when_tasks_finished: bool

    def __init__(self, stop_when_tasks_finished: bool = False):
        self.stop_when_tasks_finished = stop_when_tasks_finished

    def execute(self, thread):
        if self.stop_when_tasks_finished:
            thread.set_state(ThreadState.STOP_ON_NO_TASKS)
        else:
            thread.set_state(ThreadState.STOPPED)


class StartThread(ThreadCommand):
    def execute(self, thread):
        thread.set_state(ThreadState.RUN_TASKS)


class ThreadPool:
    threads: list[Thread]

    def __init__(self, n_threads: int):
        self.threads = [Thread(i) for i in range(n_threads)]

        for thread in self.threads:
            thread.start()

    def send_command_to_thread(self, tid, command: ThreadCommand):
        self.threads[tid].queue.put(command)

    def send_task_to_thread(self, tid, task):
        self.send_command_to_thread(tid, AddTaskToThread(task))

    def stop_all(self):
        for tid in range(len(self.threads)):
            self.send_command_to_thread(tid, StopThread())


if __name__ == '__main__':
    pool = ThreadPool(2)
    pool.send_command_to_thread(0, InspectThread())
    pool.send_command_to_thread(1, StartThread())
    pool.send_task_to_thread(1, lambda: print("hello"))
    pool.send_command_to_thread(1, InspectThread())
    pool.send_task_to_thread(0, lambda: print("hello from thread 0"))
    pool.send_task_to_thread(0, lambda: pool.send_command_to_thread(0, InspectThread()))
    print('gonna start thread 0...')
    pool.send_command_to_thread(0, StartThread())

    pool.stop_all()
