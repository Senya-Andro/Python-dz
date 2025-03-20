import requests

class YougileAPI:
    def __init__(self, base_url, auth_headers):
        self.base_url = base_url
        self.auth_headers = auth_headers

    def create_project(self, title, users):
        url = f"{self.base_url}/projects"
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(url, json=payload, headers=self.auth_headers)
        return response

    def update_project(self, project_id, title, users, deleted):
        url = f"{self.base_url}/projects/{project_id}"
        payload = {
            "title": title,
            "users": users,
            "deleted": deleted
        }
        response = requests.put(url, json=payload, headers=self.auth_headers)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.auth_headers)
        return response