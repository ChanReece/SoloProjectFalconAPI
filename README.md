# Falcon Application Skeleton

Simple boilerplate for a falcon web api

## OpenAPI Specification
There is a provided OpenAPI specification, [openapi.yaml](openapi.yaml). Currently just defines the healthcheck. Here are tools to help you expand it:
* [Specification Documentation](https://swagger.io/specification/)
* [Online Editor](https://editor.swagger.io/)
The editor will initialize with a PetStore example which is also used in the specification. This is great for learning by example.

## Usage

Do these things from your project root. The same location as this file.

Install Requirements
```bash
pip install -r requirements.txt
```

To run unit tests
```bash
python -m unittest -v
```

To get code coverage
```bash
coverage run --source=myapi -m unittest
coverage report -m
```

To serve your app with the app server gunicorn
```bash
gunicorn app:app --reload --chdir myapi/
```

With the gunicorn serving your app you can do a client integration test
```bash
python integration_tests/test_healthcheck.py
```
