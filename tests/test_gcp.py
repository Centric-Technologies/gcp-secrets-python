import pytest
from google.cloud import secretmanager
from centric.secrets.gcp import get_secret_value

class MockSecretClient:
    @staticmethod
    def access_secret_version(a):
        return 'test'
    @staticmethod
    def secret_version_path(a, b, c):
        return 'path'

class MockSecretManager:
    @staticmethod
    def SecretManagerServiceClient():
        return MockSecretClient()

def test_get_value_not_production(monkeypatch):
    monkeypatch.setenv('IS_PRODUCTION', 'False')
    monkeypatch.setenv('SECRET_NAME', 'value')
    assert get_secret_value('SECRET_NAME') == 'value'

def test_get_value_not_production_key_not_exist(monkeypatch):
    monkeypatch.setenv('IS_PRODUCTION', 'False')
    with pytest.raises(KeyError):
        get_secret_value('SECRET_NAME')

# def test_get_secret_value(monkeypatch):
#     def mock_manager(*args, **kwargs):
#         return MockSecretManager

#     monkeypatch.setenv('IS_PRODUCTION', 'True')
#     monkeypatch.setenv('GCP_PROJECT_ID', 'proj')
#     monkeypatch.setattr(secretmanager, "SecretManagerServiceClient", mock_manager)
    
#     assert get_secret_value('SECRET_NAME') == 'value'
