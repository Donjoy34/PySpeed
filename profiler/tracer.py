import sys
from collections import defaultdict

from profiler.cpu_tracker import CPUTracker
from profiler.memory_tracker import MemoryTracker


class FunctionTracer:

    def __init__(self):

        self.cpu = CPUTracker()
        self.mem = MemoryTracker()

        self.stats = defaultdict(lambda: {
            "calls": 0,
            "time": 0,
            "memory": 0
        })

    def _func_id(self, frame):

        code = frame.f_code
        filename = code.co_filename
        funcname = code.co_name

        return f"{filename}:{funcname}"

    def trace(self, frame, event, arg):

        if event == "call":

            func_id = self._func_id(frame)

            self.cpu.start(func_id)
            self.mem.start(func_id)

        elif event == "return":

            func_id = self._func_id(frame)

            duration = self.cpu.stop(func_id)
            memory = self.mem.stop(func_id)

            stat = self.stats[func_id]

            stat["calls"] += 1
            stat["time"] += duration
            stat["memory"] += memory

        return self.trace

    def start(self):
        sys.setprofile(self.trace)

    def stop(self):
        sys.setprofile(None)