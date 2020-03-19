# CONFIG.PY

"""Stores various constants and configuration settings."""

import os

# Path to this file. Currently assumes we are in the backend/ directory.
PATH_TO_CONFIG = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# Paths to data.
DATA_DIR = os.path.join(PATH_TO_CONFIG, 'data')
HP_CHARACTERS_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-characters.json')
HP_SPELLS_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-spells.json')
HP_HOUSES_FILE_PATH = os.path.join(DATA_DIR, 'harry-potter-houses.json')

# Endpoint routes.
CHARACTERS_DIR = '/characters'
SPELLS_DIR = '/spells'
HOUSES_DIR = '/houses'
CHARACTERS_ROUTE = os.path.join(CHARACTERS_DIR, '<character_id>')
SPELLS_ROUTE = os.path.join(SPELLS_DIR, '<spell_id>')
HOUSES_ROUTE = os.path.join(HOUSES_DIR, '<house_id>')

# Used when requesting all ids from a given data file.
# Note: This should also be a constant used by frontend/, so this
# should either be duplicated or config.py should be raised to the
# parent directory and appropriate steps taken to allow backend/ and
# frontend/ folders to access the file from a subdirectory.
ALL_DATA = 'all'

# Limit on cache before eviction begins.
CACHE_LIMIT = 3

