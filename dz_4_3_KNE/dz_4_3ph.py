import pytest
import requests
import random
import json
from jsonschema import validate
from random import randint

class PlaceholderTest:


    def test_ph_status_code(self):
        res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert res.status_code == 200


    def test_ph_json_utf(self):
        res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert res.headers["Content-Type"] == "application/json; charset=utf-8"


    def test_ph_json_schema(self):
        res = requests.get("https://jsonplaceholder.typicode.com/posts/1")

        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"},
                "userId": {"type": "integer"}
            },
            "required": ["id", "title", "body", "userId"]
        }
        validate(instance=res.json(), schema=schema)


    @pytest.mark.parametrize("id_comm, ind_com", [(1, 2), (2, 3), (3, 4)])
    def test_ph_comments(self, id_comm, ind_com):
        res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_comm}/comments",
                           params={'id_comm': id_comm, 'ind_com': ind_com})
        random_comment = random.randint(1, 4)
        response_body = res.json()
        assert response_body[random_comment]['postId'] == id_comm

#5 Test на возврат пользователя по id
    @pytest.mark.parametrize("id_user", [1, 12, 18])
    def test_ph_return_user_by_id(self, id_user):
        res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_user}",
                           params={'id_user': id_user})
        response_body = res.json()
        assert response_body['id'] == id_user