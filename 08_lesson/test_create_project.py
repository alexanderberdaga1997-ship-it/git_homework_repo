from project_api import ProjectApi


api = ProjectApi()


def test_create_project_positive():
    response = api.create_project("Мой тестовый проект")

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == "Мой тестовый проект"

    api.delete_project(body["id"])


def test_create_project_negative():
    response = api.create_project("")

    assert response.status_code == 400

    body = response.json()

    assert "error" in body
