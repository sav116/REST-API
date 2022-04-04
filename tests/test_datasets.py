from tests.base_test import client
from endpoints.base import prefix

request_body = {
    "id": "bac6baef-1be2-476c-944b-2980f69b27b6",
    "version": "one",
    "date": "2022-02-25T20:10:19.879861",
    "flatTabLink": "test",
    "flatTabSourceType": "df3a2d67-dacf-4ce7-8116-fa1c1596fdb0",
    "customerOrgForm": "test",
    "fileURL": "test",
    "name": "test",
    "script": "test"
}

api = prefix + '/datasets'

new_request_body = request_body.copy()
new_request_body["version"] = "two"

fake_id = 'c0230528-e7fa-4f85-813c-5b82e703f2da'


def test_create_datasets():
    response = client.post(
        api,
        json=request_body,
    )
    assert response.status_code == 201
    assert response.json() == request_body


def test_get_datasets():
    response = client.get(api)
    assert response.status_code == 200
    assert response.json() == [request_body]


def test_get_dataset_by_id():
    response = client.get(f"{api}/{request_body['id']}")
    assert response.status_code == 200
    assert response.json() == request_body


def test_get_fake_dataset():
    response = client.get(f"{api}/{fake_id}")
    assert response.status_code == 404


def test_update_dataset():
    response = client.put(f"{api}?dataset_id={request_body['id']}&version={new_request_body['version']}")
    assert response.status_code == 200
    assert response.json() == new_request_body


def test_delete_dataset():
    response = client.delete(f"{api}/{request_body['id']}")
    assert response.status_code == 200
    assert response.json() == new_request_body
