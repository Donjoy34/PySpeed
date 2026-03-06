import argparse
from cli.run_profiler import run_script


def main():

    parser = argparse.ArgumentParser(
        description="PyPulse - Python Runtime Profiler"
    )

    parser.add_argument(
        "script",
        help="Python script to profile"
    )

    args = parser.parse_args()

    print("Running:", args.script)

    run_script(args.script)


if __name__ == "__main__":
    main()