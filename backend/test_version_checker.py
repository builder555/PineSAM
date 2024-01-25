import pytest
from version_checker import VersionChecker, is_semver_greater
from unittest.mock import MagicMock, mock_open


@pytest.fixture
def mock_file_not_exist(monkeypatch):
    monkeypatch.setattr("os.path.exists", lambda path: False)


@pytest.fixture
def mock_file_exist(monkeypatch):
    monkeypatch.setattr("os.path.exists", lambda path: True)
    monkeypatch.setattr("builtins.open", mock_open(read_data="1.0.0"))


@pytest.fixture
def mock_api_response(monkeypatch):
    mock_response = MagicMock()
    mock_response.json.return_value = {"tag_name": "v2.0.0"}
    monkeypatch.setattr("requests.get", lambda url: mock_response)


@pytest.fixture
def mock_api_bad_response(monkeypatch):
    mock_response = MagicMock()
    mock_response.json.return_value = {"error": "invalid"}
    monkeypatch.setattr("requests.get", lambda url: mock_response)


def test_read_version_empty_path():
    vc = VersionChecker()
    assert vc.read_version() == ""


def test_read_version_non_existent_file(mock_file_not_exist):
    vc = VersionChecker(file_path="nonexistent/path")
    assert vc.read_version() == ""


def test_read_version_existing_file(mock_file_exist):
    vc = VersionChecker(file_path="path/to/version_file")
    assert vc.read_version() == "1.0.0"


def test_get_latest_version_with_bad_api_response_returns_file_version(
    mock_file_exist, mock_api_bad_response
):
    vc = VersionChecker(file_path="path/to/version_file")
    assert vc.get_latest_version() == "1.0.0"


def test_get_latest_version_with_api_url(mock_api_response):
    vc = VersionChecker(api_url="http://api.url")
    assert vc.get_latest_version() == "2.0.0"


def test_versions_higher():
    assert is_semver_greater("1.0.0", "0.0.0") == True
    assert is_semver_greater("0.1.0", "0.0.0") == True
    assert is_semver_greater("0.0.1", "0.0.0") == True
    assert is_semver_greater("0.2.0", "0.0.9") == True
    assert is_semver_greater("0.0.10", "0.0.9") == True
    assert is_semver_greater("1.0.0", "0.99.99") == True
    assert is_semver_greater("1.12.0", "1.11.9") == True


def test_versions_lower():
    assert is_semver_greater("0.2.0", "1.0.0") == False
    assert is_semver_greater("0.0.9", "0.1.0") == False
    assert is_semver_greater("0.0.9", "0.0.10") == False
    assert is_semver_greater("1.11.9", "1.12.0") == False
    assert is_semver_greater("1.11.9", "1.11.10") == False
    assert is_semver_greater("0.99.99", "1.0.0") == False


def test_versions_equal():
    assert is_semver_greater("0.0.0", "0.0.0") == False
    assert is_semver_greater("1.0.0", "1.0.0") == False
    assert is_semver_greater("0.1.0", "0.1.0") == False
    assert is_semver_greater("0.0.1", "0.0.1") == False
    assert is_semver_greater("0.2.0", "0.2.0") == False
    assert is_semver_greater("0.0.10", "0.0.10") == False
    assert is_semver_greater("1.12.3", "1.12.3") == False
