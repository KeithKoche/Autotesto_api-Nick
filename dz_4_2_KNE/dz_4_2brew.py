import pytest
import requests
import random
import json
from pytest import fixture
from jsonschema import validate
from random import randint


class BrewTest:

    def test_brew_status_code(self):
        res = requests.get("https://api.openbrewerydb.org/breweries")
        assert res.status_code == 200

    def test_app_json_brew_utf(self):
        res = requests.get("https://api.openbrewerydb.org/breweries")
        assert res.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_brew_json_schema(self):
        res = requests.get("https://api.openbrewerydb.org/breweries")

        schema = {
            "type": "array",
            "items": [
                    {"type": "object",
                        "properties": {
                                        "id": {"type": "integer"},
                                        "address_2": {"type": "null"},
                                        "address_3": {"type": "null"},
                                        "county_province": {"type": "null"},
                                        "additionalProperties": {"type": "string"}
                                        },
                            "required": ["id", "name", "brewery_type"]
                     }
                    ]
                }
        validate(instance=res.json(), schema=schema)


    @pytest.mark.parametrize('id', [7760, 4389, 1718])
    def test_single_brew_by_id(self, id):
        res = requests.get(f"https://api.openbrewerydb.org/breweries/{id}",
                       params={'id': id})
        response_body = res.json()
        assert response_body['id'] == id


    @pytest.mark.parametrize("b_city, bp", [('Livermore', 2), ('San Diego', 3)])
    def test_brew_by_city_names(self, b_city, bp):
        res = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={b_city}",
                       params={'b_city': b_city, 'bp': bp})
        random_ind = random.randint(2, 3)
        response_body = res.json()
        assert response_body[random_ind]['city'] == b_city