from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'marcelo',
            'email': 'marcelo@email.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    print('response ---->', response.json())
    assert response.json() == {
        'username': 'marcelo',
        'email': 'marcelo@email.com',
        'id': 1,
    }
