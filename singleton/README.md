# singleton
singletone decorator provider

## Example
``` python
import singleton
@singleton.singletonDecorator
class Foo:
    def __init__(self, x:int)->None:
        self.x = x
assert id(Foo(15)) == id(Foo(20))

## Setup
```sh
poetry install

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
