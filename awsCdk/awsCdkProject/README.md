# awsCdkProject
poetry export -f requirements.txt --without-hashes -o requirements.txt
poetry run pip install . -r requirements.txt -t package
cd package ; zip -r ../artifact.zip . -x '*.pyc'
## Setup
```sh
poetry install

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
