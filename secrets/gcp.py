import os
from google.cloud import secretmanager

project_name = os.environ('GCP_PROJECT_ID')
is_production = os.environ['IS_PRODUCTION'] == "True"
if is_production:
    secret_client = secretmanager.SecretManagerServiceClient()

def get_secret_value(secret_name, version='latest'):
    #TODO store secret on redis for a short time?
    if is_production:
        full_path = secret_client.secret_version_path(project_name, secret_name, version)
        return secret_client.access_secret_version(full_path).payload.data.decode('UTF-8')
    
    return os.environ[secret_name.upper()]
