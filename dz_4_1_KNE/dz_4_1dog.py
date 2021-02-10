import pytest
import requests
import json
from jsonschema import validate

class DogTest:


    def test_status_code(self):
        res = requests.get("https://dog.ceo/api/breeds/list/all")
        assert res.status_code == 200


    def test_list_all_breeds_app_j(self):
        res = requests.get("https://dog.ceo/api/breeds/list/all")
        assert res.headers["Content-Type"] == "application/json"


    def test_list_all_breeds_schema(self):
        res = requests.get("https://dog.ceo/api/breeds/list/all")

        schema = {
            "type": "object",
            "properties": {
                    "message": {
                    "type": "object",
                    "additionalProperties": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
          },
                    "status": {
                    "type": "string"
                }
            },
            "required": ["message", "status"]
        }
        validate(instance=res.json(), schema=schema)


    @pytest.mark.parametrize("single_breed", ["zhoochka"])
    def test_breed_not_exists(self, single_breed):
        res = requests.get(f"https://dog.ceo/api/breed/{single_breed}/images",
                       params={'single_breed': single_breed})
        response_body = res.json()
        assert response_body["message"] == "Breed not found (master breed does not exist)"
        assert response_body["status"] == "error"
        assert response_body["code"] == 404


    @pytest.mark.parametrize('dog, subdog', [("bulldog", ['boston', 'english', 'french']),
                                         ("mountain", ['bernese', 'swiss'])])
    def test_some_subbreed(self, dog, subdog):
        res = requests.get(f"https://dog.ceo/api/breed/{dog}/list",
                      params={'dog': dog})
        response_body = res.json()
        assert response_body['message'] == subdog
        assert response_body['status'] == 'success'