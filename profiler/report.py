from profiler import tracer
from profiler.exporter import export_json


export_json(tracer.stats)
def generate_report(stats):

    print("\nPyPulse Performance Report\n")

    print(f"{'Function':40} {'Calls':10} {'Total Time (s)':15} {'Memory (KB)':15}")
    print("-" * 80)

    for func, data in sorted(stats.items(), key=lambda x: x[1]["time"], reverse=True):

        print(
            f"{func[:38]:40} "
            f"{data['calls']:10} "
            f"{data['time']:.6f} "
            f"{data['memory']:.2f}"
        )