# API.PY

import config
import utils
from cache import Cache

from flask import Flask, request, jsonify, abort


def create_app():
    app = Flask(__name__)
    cache = Cache(config.CACHE_LIMIT) 

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
        """
        return response.replace('\n', '<br>')

    @app.route(config.CHARACTERS_ROUTE)
    def character_request(character_id):
        """GET request for character information.
        Input: Unique character id or 'all' for a list of all character ids.
        Output: Json containing character information.
        """
        name = request.args.get("character_id", character_id)
        data = utils.get_data(character_id, config.HP_CHARACTERS_FILE_PATH, cache)
        if not data:
            abort(404, description=f'Invalid character id: {character_id}.')
        return jsonify(data)

    @app.route(config.SPELLS_ROUTE)
    def spell_request(spell_id):
        """GET request for spell information.
        Input: Unique spell id or 'all' for a list of all spell ids.
        Output: Json containing spell information.
        """
        spell_id = request.args.get('spell_id', spell_id)
        data = utils.get_data(spell_id, config.HP_SPELLS_FILE_PATH, cache)
        if not data:
            abort(404, description=f'Invalid spell id: {spell_id}.')
        return jsonify(data)

    @app.route(config.HOUSES_ROUTE)
    def house_request(house_id):
        """GET request for house information.
        Input: Unique house id or 'all' for a list of all house ids.
        Output: Json containing house information.
        """
        house_id = request.args.get('house_id', house_id)
        data = utils.get_data(house_id, config.HP_HOUSES_FILE_PATH, cache)
        if not data:
            abort(404, description=f'Invalid house id: {house_id}.')
        return jsonify(data)
     
    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error=str(e)), 404

    return app

# Create the app. Note that we wrapped everything into
# a create_app function to make unit testing as painless
# as possible.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

