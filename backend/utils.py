# UTILS.PY

import config
import json

def _load_json(filename, cache):
    # Loads json file, storing it in cache if needed.
    # _ prefix implies that functions interacting with
    # cache contents should not be called outside of utils.py.
    data = cache.get(filename)
    if not data:
        with open(filename) as f:
            data = json.load(f)
        cache.add(filename, data)
    return data

def get_data(item_id, filename, cache):
    data = _load_json(filename, cache) 

    # Special case: Return all ids.
    if item_id == config.ALL_DATA:
        return [entity['_id'] for entity in data]
    
    for entity in data:
        if entity['_id'] == item_id:
            return entity

    # Not found.
    return None

if __name__ == '__main__':
    print('WARNING: Running utils.py.')

