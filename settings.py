from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import pathlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = pathlib.Path(BASE_DIR).joinpath("data")
DATA_DIR.mkdir(exist_ok=True)
