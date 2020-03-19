# API.PY

import config
import utils
import cache

from flask import Flask, request, jsonify, abort


app = Flask(__name__)
cache = Cache(CACHE_LIMIT) 

@app.route('/')
def help():
    """A blank request will return instructions on how to use the API."""
    response = """
    Potential API calls:
    Get all character/spell/house ids:
        GET /characters/all
        GET /spells/all
        GET /houses/all
    
    Get data specific to a particular id:
        GET /your-desired-category/item-id

    Front end interaction:
    Go to any of the following:
        /characters/
        /spells/
        /houses/
    ...and there will be a list for each which uses the provided API.

    """
    return response.replace('\n', '<br>')

@app.route('/characters/<character_id>')
def character_request(character_id):
    """Request for character information.
    Input: Unique character id or '-1' for a list of all character ids.
    Output: Json containing"""
    name = request.args.get("character_id", character_id)
    data = utils.get_data(character_id, config.HP_CHARACTERS_FILE_PATH, cache)
    if not data:
        abort(404, description=f"Invalid character id: {character_id}.")
    return jsonify(data)

@app.route('/spells/<spell_id>')
def spell_request(spell_id):
    """ TODO docstring """
    spell_id = request.args.get("spell_id", spell_id)
    data = utils.get_data(spell_id, config.HP_SPELLS_FILE_PATH, cache)
    if not data:
        abort(404, description=f"Invalid spell id: {spell_id}.")
    return jsonify(data)

@app.route('/houses/<house_id>')
def house_request(house_id):
    """ TODO docstring """
    house_id = request.args.get("house_id", house_id)
    data = utils.get_data(house_id, config.HP_HOUSES_FILE_PATH, cache)
    if not data:
        abort(404, description=f"Invalid house id: {house_id}.")
    return jsonify(data)
 
@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404
     
