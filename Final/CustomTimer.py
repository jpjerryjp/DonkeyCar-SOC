import threading
import time


class CustomTimer(threading.Thread):

    def __init__(self, interval, funct):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        self.interval = interval
        self.function = funct
        super().__init__()

    def run(self):
        while self._timer_runs.is_set():
            self.function()
            time.sleep(self.interval)

    def stop(self):
        self._timer_runs.clear()