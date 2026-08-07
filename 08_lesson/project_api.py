import requests

from config import BASE_URL, TOKEN


class ProjectApi:
    def __init__(self):
        self.url = f"{BASE_URL}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        }

    def create_project(self, title):
        body = {
            "title": title,
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            json=body,
        )

        return response

    def update_project(self, project_id, title):
        body = {
            "title": title,
        }

        response = requests.put(
            f"{self.url}/{project_id}",
            headers=self.headers,
            json=body,
        )

        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.url}/{project_id}",
            headers=self.headers,
        )

        return response

    def delete_project(self, project_id):
        response = requests.delete(
            f"{self.url}/{project_id}",
            headers=self.headers,
        )

        return response
