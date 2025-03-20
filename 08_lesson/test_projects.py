import pytest

@pytest.fixture
def api_client(base_url, auth_headers):
    return YougileAPI(base_url, auth_headers)

def test_create_project_positive(api_client):
    title = "ГосУслуги"
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
    response = api_client.create_project(title, users)
    assert response.status_code == 201
    assert response.json()["title"] == title

def test_create_project_negative(api_client):
    title = ""
    users = {}
    response = api_client.create_project(title, users)
    assert response.status_code == 400

def test_update_project_positive(api_client):
    project_id = "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"
    title = "ГосУслуги"
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
    deleted = True
    response = api_client.update_project(project_id, title, users, deleted)
    assert response.status_code == 200
    assert response.json()["deleted"] == deleted

def test_update_project_negative(api_client):
    project_id = "invalid_id"
    title = "ГосУслуги"
    users = {}
    deleted = True
    response = api_client.update_project(project_id, title, users, deleted)
    assert response.status_code == 404

def test_get_project_positive(api_client):
    project_id = "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"
    response = api_client.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_negative(api_client):
    project_id = "invalid_id"
    response = api_client.get_project(project_id)
    assert response.status_code == 404