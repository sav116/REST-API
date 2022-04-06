from tests.base_test import client
from endpoints.base import prefix

api = prefix + '/s3_api'
s3_test_folder = '/test_data'

test_file_name = 'dump.sql'

test_file_1 = 'tests/test_data/data1.txt'
test_file_2 = 'tests/test_data/data1.txt'


def test_upload_file():
    with open(test_file_1, 'rb') as f:
        body = f.read()
        response = client.post(
            api + s3_test_folder,
            files={
                "files": (
                    'dump.sql',
                    body,
                    "multipart/form-data")})
        assert response.status_code == 201


def test_get_file():
    response = client.get(
        api +
        '/file' +
        s3_test_folder +
        '%2F' +
        test_file_name)
    assert response.status_code == 200


def test_get_file_names():
    response = client.get(api + '/directory' + s3_test_folder)
    assert response.status_code == 200


def test_update_file():
    with open(test_file_2, 'rb') as f:
        body = f.read()
        response = client.put(
            api +
            s3_test_folder +
            '%2F' +
            test_file_1,
            files={
                "files": (
                    test_file_1,
                    body,
                    "multipart/form-data")})
        assert response.status_code == 200


def test_delete_file():
    response = client.delete(api + s3_test_folder + '%2F' + test_file_name)
    assert response.status_code == 200
