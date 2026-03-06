import time


class CPUTracker:

    def __init__(self):
        self.start_times = {}

    def start(self, func_id):
        self.start_times[func_id] = time.perf_counter()

    def stop(self, func_id):

        if func_id not in self.start_times:
            return 0

        duration = time.perf_counter() - self.start_times.pop(func_id)

        return duration