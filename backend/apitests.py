# APITESTS.PY

"""Basic functionality testing for provided API endpoints."""

import config
import os
import json
import unittest
import api

from flask import Flask

try:
    from flask_testing import TestCase
except ImportError as e:
    print("PLEASE RUN 'pip install Flask-Testing'.")


class TestCharactersEndpoint(TestCase):
    def create_app(self):
        # Note: Since we do not pull the cache into our test,
        # all cache calls done by our app will return None, so
        # our app always loads from disk for the purpose of testing.
        # This is intended, as cache functionality should be tested
        # separately (as it is). Ditto for other endpoint tests.
        return api.create_app()

    def test_all_data(self):
        # Ensure the correct keys are returned.
        all_route = os.path.join(config.CHARACTERS_DIR, config.ALL_DATA)
        response = self.client.get(all_route)
        with open(config.HP_CHARACTERS_FILE_PATH) as f:
            actual = json.load(f)
        self.assertEqual(response.json, [entity['_id'] for entity in actual])

    def test_valid_request(self):
        valid_id = '5a0fa4daae5bc100213c232e'
        expected = {"_id":"5a0fa4daae5bc100213c232e","name":"Hannah Abbott",
                    "role":"student","house":"Hufflepuff",
                    "school":"Hogwarts School of Witchcraft and Wizardry",
                    "__v":0,"ministryOfMagic":False,"orderOfThePhoenix":False,
                    "dumbledoresArmy":True,"deathEater":False,
                    "bloodStatus":"half-blood","species":"human"}

        valid_route = os.path.join(config.CHARACTERS_DIR, valid_id)
        response = self.client.get(valid_route)
        
        self.assertEqual(response.json, expected)

    def test_invalid_request(self):
        invalid_id = 'invalid'
        expected = {'error': f'404 Not Found: Invalid character id: {invalid_id}.'}

        invalid_route = os.path.join(config.CHARACTERS_DIR, invalid_id)
        response = self.client.get(invalid_route)

        self.assertEqual(response.json, expected)


class TestSpellsEndpoint(TestCase):
    def create_app(self):
        return api.create_app()

    def test_all_data(self):
        # Ensure the correct keys are returned.
        all_route = os.path.join(config.SPELLS_DIR, config.ALL_DATA)
        response = self.client.get(all_route)
        with open(config.HP_SPELLS_FILE_PATH) as f:
            actual = json.load(f)
        self.assertEqual(response.json, [entity['_id'] for entity in actual])

    def test_valid_request(self):
        valid_id = '5b74ebd5fb6fc0739646754c'
        expected = {"_id":"5b74ebd5fb6fc0739646754c","spell":"Aberto",
                    "type":"Charm","effect":"opens objects"}

        valid_route = os.path.join(config.SPELLS_DIR, valid_id)
        response = self.client.get(valid_route)

        self.assertEqual(response.json, expected)
 
    def test_invalid_request(self):
        invalid_id = 'invalid'
        expected = {'error': f'404 Not Found: Invalid spell id: {invalid_id}.'}

        invalid_route = os.path.join(config.SPELLS_DIR, invalid_id)
        response = self.client.get(invalid_route)

        self.assertEqual(response.json, expected)
      

class TestHousesEndpoint(TestCase):
    def create_app(self):
        return api.create_app()

    def test_all_data(self):
        # Ensure the correct keys are returned.
        all_route = os.path.join(config.HOUSES_DIR, config.ALL_DATA)
        response = self.client.get(all_route)
        with open(config.HP_HOUSES_FILE_PATH) as f:
            actual = json.load(f)
        self.assertEqual(response.json, [entity['_id'] for entity in actual])

    def test_valid_request(self):
        valid_id = '5a05dc58d45bd0a11bd5e070'
        expected = {"_id":"5a05dc58d45bd0a11bd5e070","name":"Hufflepuff",
                    "mascot":"badger","headOfHouse":"Pomona Sprout",
                    "houseGhost":"The Fat Friar","founder":"Helga Hufflepuff",
                    "__v":0,"school":"Hogwarts School of Witchcraft and Wizardry",
                    "members":["5a0fa11a4d153d00212c47cc","5a0fa360ae5bc100213c232c",
                    "5a0fa365ae5bc100213c232d","5a0fa4daae5bc100213c232e","5a0fa842ae5bc100213c2339",
                    "5a0fa86dae5bc100213c233a","5a1096253dc2080021cd875f","5a1098bd3dc2080021cd876d",
                    "5a109c993dc2080021cd8783","5a1223720f5ae10021650d6f","5a1223ed0f5ae10021650d70",
                    "5a122f3d0f5ae10021650d8d","5a1232b10f5ae10021650d95","5a12333f0f5ae10021650d96",
                    "5a1234500f5ae10021650d99","5a1235790f5ae10021650d9d","5a123cb40f5ae10021650dbc"],
                    "values":["hard work","patience","justice","loyalty"],"colors":["yellow","black"]}

        valid_route = os.path.join(config.HOUSES_DIR, valid_id)
        response = self.client.get(valid_route)

        self.assertEqual(response.json, expected)
  
    def test_invalid_request(self):
        invalid_id = 'invalid'
        expected = {'error': f'404 Not Found: Invalid house id: {invalid_id}.'}

        invalid_route = os.path.join(config.HOUSES_DIR, invalid_id)
        response = self.client.get(invalid_route)

        self.assertEqual(response.json, expected)
    

if __name__ == '__main__':
    unittest.main()
