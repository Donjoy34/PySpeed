import json

def export_json(stats):

    output = {}

    for func, data in stats.items():

        name = func.split(":")[-1]

        output[name] = {
            "time": data["time"],
            "memory": data["memory"],
            "calls": data["calls"]
        }

    with open("pyspeed_profile.json", "w") as f:
        json.dump(output, f, indent=2)