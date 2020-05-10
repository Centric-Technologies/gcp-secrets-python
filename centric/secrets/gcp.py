import os
from google.cloud import secretmanager

def get_secret_value(secret_name, version='latest'):
    is_production = os.getenv('IS_PRODUCTION', 'False') == "True"
    if not is_production:
        return os.environ[secret_name.upper()]
    
    secret_client = secretmanager.SecretManagerServiceClient()
    full_path = secret_client.secret_version_path(os.environ['GCP_PROJECT_ID'],
        secret_name, version)
    
    return secret_client.access_secret_version(full_path).payload.data.decode('UTF-8')
    
