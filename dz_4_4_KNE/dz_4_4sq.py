import pytest
import requests

def test_valide_status_code(url_static, g_method, st_code):
    target = url_static
    response = g_method(url=target)
    assert response.status_code == st_code