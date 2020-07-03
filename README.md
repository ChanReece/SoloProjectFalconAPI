# falcon-skeleton
Simple boilerplate for a falcon web api

Do these things from your project root. The same location as this file.

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
