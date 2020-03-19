# CONFIG.PY

"""Stores various constants and configuration settings."""

import os

# Path to this file. Currently assumes we are in the backend/ directory.
# In an ideal world, config.py is in the top level directory. TODO.
PATH_TO_CONFIG = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# Paths to data.
DATA_DIR = os.path.join(PATH_TO_CONFIG, 'data')
HP_CHARACTERS_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-characters.json')
HP_SPELLS_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-spells.json')
HP_HOUSES_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-houses.json')

# Used when requesting all ids from a given data file.
ALL_DATA = 'all'
