from project_api import ProjectApi


api = ProjectApi()


def test_get_project_positive():
    create_response = api.create_project("Проект для получения")

    project_id = create_response.json()["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == project_id
    assert body["title"] == "Проект для получения"

    api.delete_project(project_id)


def test_get_project_negative():
    response = api.get_project("123456789")

    assert response.status_code == 404

    body = response.json()

    assert "error" in body
