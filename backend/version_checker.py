import requests
import os


class VersionChecker:
    def __init__(self, file_path: str = "", api_url: str = ""):
        self.file_path = file_path
        self.api_url = api_url

    def read_version(self):
        if not (self.file_path and os.path.exists(self.file_path)):
            return ""
        with open(self.file_path) as f:
            return f.read().strip()

    def get_latest_version(self):
        response = requests.get(self.api_url).json()
        return response.get("tag_name", self.read_version()).strip("v")


def is_semver_greater(v1, v2):
    v1 = list(map(int, v1.split(".")))
    v2 = list(map(int, v2.split(".")))
    return v1 > v2
