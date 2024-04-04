from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.project import create_random_project
from app.tests.utils.utils import dict_is_subset


SAMPLE_DATA = {
    'name': 'Example test 🚀',
    'description': "Some description",
    'date_range': {
        'lower': '2021-01-01',
        'upper': '2021-01-02'
    },
    "area_of_interest": {"field1": "ok"}
}


def test_create_project(
    client: TestClient, db: Session
) -> None:
    response = client.post(
        f"{settings.API_V1_PATH}/projects/", json=SAMPLE_DATA,
    )

    assert response.status_code == 201
    content = response.json()
    assert 'id' in content
    assert dict_is_subset(content, SAMPLE_DATA)


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
    create_random_project(db)
    create_random_project(db)
    response = client.get(f"{settings.API_V1_PATH}/projects")
    assert response.status_code == 200

    content = response.json()
    assert 'items' in content
    assert len(content['items']) >= 2


def test_update_project(client: TestClient, db: Session):
    project = create_random_project(db)

    response = client.put(
        f"{settings.API_V1_PATH}/projects/{project.id}", json=SAMPLE_DATA,
    )

    assert response.status_code == 200
    content = response.json()
    assert 'id' in content
    assert dict_is_subset(content, SAMPLE_DATA)


def test_delete_project(client: TestClient, db: Session):
    project = create_random_project(db)
    response = client.delete(f"{settings.API_V1_PATH}/projects/{project.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == project.id

    response_get = client.get(f"{settings.API_V1_PATH}/projects/{project.id}")
    assert response_get.status_code == 404
