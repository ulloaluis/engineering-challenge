# UTILS.PY

import config
import json

def get_data(item_id, filename):
    with open(filename) as f:
        data = json.load(f)

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

