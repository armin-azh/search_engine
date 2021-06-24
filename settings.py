from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import pathlib
import configparser

conf = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conf.read(os.path.join(BASE_DIR, "conf.ini"))

DATA_DIR = pathlib.Path(BASE_DIR).joinpath("data")
DATA_DIR.mkdir(exist_ok=True)

STORAGE_DIR = DATA_DIR.joinpath('storage')
STORAGE_DIR.mkdir(exist_ok=True)
