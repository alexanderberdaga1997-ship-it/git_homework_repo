from project_api import ProjectApi


api = ProjectApi()


def test_update_project_positive():
    create_response = api.create_project("Старое название")

    project_id = create_response.json()["id"]

    response = api.update_project(
        project_id,
        "Новое название"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["title"] == "Новое название"

    api.delete_project(project_id)


def test_update_project_negative():
    response = api.update_project(
        "123456789",
        "Название"
    )

    assert response.status_code == 404

    body = response.json()

    assert "error" in body
