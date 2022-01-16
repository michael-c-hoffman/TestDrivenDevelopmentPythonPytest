import os
import pytest


def mypyTests(args=None):
    pytest.main(["--mypy",  "-m", "mypy"])

def isortTests():
    pytest.main(["--isort", "-m", "isort"])

def blackTests():
    pytest.main(["--black", "-m", "black"])

def flake8Tests():
    pytest.main(["--flake8", "-m", "flake8"])
