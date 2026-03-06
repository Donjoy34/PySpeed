from rich.live import Live
from rich.table import Table
from rich.console import Console
import time


class LiveDashboard:

    def __init__(self, stats):

        self.stats = stats
        self.console = Console()

    def build_table(self):

        table = Table(title="PySpeed Live Profiler")

        table.add_column("Function", style="cyan")
        table.add_column("Calls", justify="right")
        table.add_column("Time (s)", justify="right")
        table.add_column("Memory (KB)", justify="right")

        for func, data in sorted(
            self.stats.items(),
            key=lambda x: x[1]["time"],
            reverse=True
        ):

            table.add_row(
                func[:40],
                str(data["calls"]),
                f"{data['time']:.4f}",
                f"{data['memory']:.2f}"
            )

        return table

    def run(self):

        with Live(self.build_table(), refresh_per_second=2) as live:

            while True:
                live.update(self.build_table())
                time.sleep(0.5)