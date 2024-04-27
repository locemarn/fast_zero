from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app, delete_user, update_user


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
    assert response.json() == {
        'username': 'marcelo',
        'email': 'marcelo@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'marcelo',
                'email': 'marcelo@email.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_exception(client):
    with pytest.raises(Exception) as e:
        update_user(12, {})
    assert e.value.status_code == HTTPStatus.NOT_FOUND
    assert e.value.detail == 'User not found'


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_exception(client):
    with pytest.raises(Exception) as e:
        delete_user(12)
    assert e.value.status_code == HTTPStatus.NOT_FOUND
    assert e.value.detail == 'User not found'
