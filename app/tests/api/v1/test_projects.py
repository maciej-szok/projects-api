from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.project import create_random_project


def test_create_project(
    client: TestClient, db: Session
) -> None:
    data = {
        'name': 'Example test 🚀',
        'description': "Some description",
        'date_range': {
            'lower': '2021-01-01', 
            'upper': '2021-01-02'
        },
        "area_of_interest": {"field1": "ok"}
    }

    response = client.post(
        f"{settings.API_V1_PATH}/projects/", json=data,
    )

    assert response.status_code == 201
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["date_range"]['lower'] == data["date_range"]['lower']
    assert content["date_range"]['upper'] == data["date_range"]['upper']
    assert content["area_of_interest"] == data["area_of_interest"]
    assert 'id' in content


def test_read_project(
    client: TestClient, db: Session
) -> None:
    project = create_random_project(db)
    response = client.get(f"{settings.API_V1_PATH}/projects/{project.id}")
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == project.name
    assert content["description"] == project.description
    assert content["date_range"]['lower'] == str(project.date_range.lower)
    assert content["date_range"]['upper'] == str(project.date_range.upper)
    assert content["id"] == project.id


def test_read_projects(
    client: TestClient, db: Session
) -> None:
    project1 = create_random_project(db)
    project2 = create_random_project(db)
    response = client.get(f"{settings.API_V1_PATH}/projects")
    assert response.status_code == 200

    content = response.json()
    assert 'items' in content


def test_update_project(client: TestClient, db: Session):
    project = create_random_project(db)
    data = {
        'name': 'Example test 🚀',
        'description': "Some description",
        'date_range': {
            'lower': '2021-01-01',
            'upper': '2021-01-02'
        },
        "area_of_interest": {"field1": "ok"}
    }

    response = client.put(
        f"{settings.API_V1_PATH}/projects/{project.id}", json=data,
    )

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["date_range"]['lower'] == data["date_range"]['lower']
    assert content["date_range"]['upper'] == data["date_range"]['upper']
    assert content["area_of_interest"] == data["area_of_interest"]
    assert 'id' in content


def test_delete_project(client: TestClient, db: Session):
    project = create_random_project(db)
    response = client.delete(f"{settings.API_V1_PATH}/projects/{project.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == project.id

    response_get = client.get(f"{settings.API_V1_PATH}/projects/{project.id}")
    assert response_get.status_code == 404
