import tracemalloc


class MemoryTracker:

    def __init__(self):

        tracemalloc.start()
        self.snapshots = {}

    def start(self, func_id):

        self.snapshots[func_id] = tracemalloc.take_snapshot()

    def stop(self, func_id):

        if func_id not in self.snapshots:
            return 0

        start_snapshot = self.snapshots.pop(func_id)
        end_snapshot = tracemalloc.take_snapshot()

        stats = end_snapshot.compare_to(start_snapshot, "lineno")

        memory = sum(stat.size_diff for stat in stats)

        return memory / 1024