import os
from config import base_dir

def run_build(name):
    return os.system("docker-compose -f {0}/{1}/docker-compose.yml up".format(base_dir, name))