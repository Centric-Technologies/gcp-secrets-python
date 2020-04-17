import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcp-secrets-python",
    version="0.1.0",
    author="Centric Technologies LTD",
    author_email="info@centric.bg",
    description="Allows convenient wrapper around Google Cloud Secrets Manager",
    long_description=long_description,
    url="https://github.com/Centric-Technologies/gcp-secrets-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'google-cloud-secret-manager'
    ]
)
