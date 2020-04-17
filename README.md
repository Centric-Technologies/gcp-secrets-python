# Google Cloud Secret Manager Wrapper
This package is a python 3 wrapper on top of Google Cloud Secret Manager

# Features
1. Pull a secret value from Google Cloud Secret Manager (GCSM)
2. Use environment variable instead of GCSM, if a corresponding env var is set

# How to use
## Installation
This package is still not hosted anywhere. Therefore, use the following pip command to install the package
```
pip install git+ssh://git@github.com/Centric-Technologies/gcp-secrets-python.git
```

for requirements file, use the same path.

## Before you start
This package depends on two environemnt variables to work propertly
- GCP_PROJECT_ID - The project ID in Google Cloud. Default: None
- IS_PRODUCTION - flag to use GCSM or local environment. Default: True

## Methods
```
get_secret_value(secret_name, version='latest')
```
Return a string value of 

secret_name - The key of the secret, without the project id or version (not the full path)  
version - The version to retrieve. If not set, latest will be retrieved.

## Usage

```
import centric.secrets.gcp

value = gcp.get_secret_value("password") #returns '123456''
```