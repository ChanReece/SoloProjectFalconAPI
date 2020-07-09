# Falcon Application Skeleton

Simple boilerplate for a falcon web api

## OpenAPI Specification
There is a provided OpenAPI specification, [openapi.yaml](openapi.yaml). Currently just defines the healthcheck. Here are tools to help you expand it:
* [Specification Documentation](https://swagger.io/specification/)
* [Online Editor](https://editor.swagger.io/)
The editor will initialize with a PetStore example which is also used in the specification. This is great for learning by example.

## Usage

### Using a Terminal
Do these things in a terminal from your project root. The same location as this file. Make sure your virtual environment is active.

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

To serve your app with a WSGI development server
```bash
python myapi/app.py
```

With your app running behind a server run the integration test
```bash
python integration_tests/test_healthcheck.py
```

Optional: Instead of a Dev server use Gunicorn, a production-ready server which supports threading and other advanced features.
```bash
pip install gunicorn
gunicorn app:app --reload --chdir myapi/
```

### Using VSCode

#### Setup
Setup venv
```
python3 -m venv ./.venv
. ./.venv/bin/activate
pip install --upgrade pip
```

Using venv
```
. ./.venv/bin/activate
```

Install Python Extension
```
⇧⌘X -> Search Python -> Install
``` 

Select Python Interpreter (Already configured)
```
⇧⌘P -> Python: Select Interpreter -> Select the venv interpreter (e.g. ./.venv/bin/python)
```

Setup Test (Already configured)
```
⇧⌘P -> Python: Configure Tests -> unittest -> <follow prompt>

```

#### Using
Debug app
```
Select `Python: App` -> F5
```
Place `breakpoints` as necessary, make web requests to exercise code path

Run/Debug test
```
Open test file (`tests/test_<filename>`) -> Run/Debug
```
Place `breakpoints` as necessary, works in both `tests` and `myapi` source file
