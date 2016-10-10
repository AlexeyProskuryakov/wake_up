import json
import logging
import os

import sys

S_BAD = "BAD"
S_OK = "OK"

log = logging.getLogger("wake_up_main")


def module_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(
            sys.executable
        )
    return os.path.dirname(__file__)


class ConfigManager(object):
    def __init__(self):
        config_file = os.path.join(os.environ.get("OPENSHIFT_DATA_DIR"),os.environ.get("config_file", None))

        if not config_file:
            config_file = "%s/config.json" % module_path()
        try:
            f = open(config_file, )
        except Exception as e:
            log.exception(e)
            sys.exit(-1)

        self.config_data = json.load(f)

    def get(self, name, type=str):
        if name in self.config_data:
            return type(self.config_data.get(name))
