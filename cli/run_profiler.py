import runpy
import sys
import os
import threading

sys.path.append(os.getcwd())

from profiler.tracer import FunctionTracer
from profiler.report import generate_report
from profiler.dashboard import LiveDashboard
from profiler.exporter import export_json


def run_script(script_path):

    tracer = FunctionTracer()

    dashboard = LiveDashboard(tracer.stats)

    dashboard_thread = threading.Thread(
        target=dashboard.run,
        daemon=True
    )

    dashboard_thread.start()

    tracer.start()

    runpy.run_path(script_path)

    tracer.stop()

    generate_report(tracer.stats)