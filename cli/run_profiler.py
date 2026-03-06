import runpy
import sys
import os

sys.path.append(os.getcwd())

from profiler.tracer import FunctionTracer
from profiler.report import generate_report


def run_script(script_path):
    print("Starting profiler...")

    tracer = FunctionTracer()

    tracer.start()

    runpy.run_path(script_path)

    tracer.stop()

    print("Execution finished\n")

    generate_report(tracer.stats)