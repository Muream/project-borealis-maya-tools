import os
import json

tools_dir = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(tools_dir, "config.json")


def get_config():
    with open(CONFIG_FILE, "r") as f:
        settings = json.loads(f.read())
    return settings


def write_config(config):
    dump = json.dumps(config, indent=2)
    with open(CONFIG_FILE, "w") as f:
        f.write(dump)
