import json
import logging
import os

import sys

S_BAD = "BAD"
S_OK = "OK"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s[%(levelname)s]%(name)s|%(processName)s(%(process)d): %(message)s')
formatter_process = logging.Formatter('%(asctime)s[%(levelname)s]%(name)s|%(processName)s: %(message)s')
formatter_human = logging.Formatter('%(asctime)s[%(levelname)s]%(name)s|%(processName)s: %(message)s')

sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)


def module_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(
            sys.executable
        )
    return os.path.dirname(__file__)


class ConfigManager(object):
    def __init__(self):
        config_file = os.environ.get("config-file", None)
        if not config_file:
            config_file = "%s/config.json" % module_path()
        try:
            f = open(config_file, )
        except Exception as e:
            logger.exception(e)
            sys.exit(-1)

        self.config_data = json.load(f)

    def get(self, name, type=str):
        if name in self.config_data:
            return type(self.config_data.get(name))
