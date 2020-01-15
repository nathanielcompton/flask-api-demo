# Python Web API Coding Demonstration
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Black Formatter](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Codecov](https://img.shields.io/codecov/c/github/nathanielcompton/python-api-demo)
[![Github Actions](https://github.com/nathanielcompton/python-api-demo/workflows/Python%20API%20Demo%20App/badge.svg)](https://github.com/nathanielcompton/python-api-demo)
![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fwww.github.com%2Fnathanielcompton%2Fpython-api-demo)

This project is meant to demonstrate my ability to create a web-based API server using pre-defined
[functional requirements][reqs_doc].
The initial project scope took a weekend to create, and revisions will remain ongoing
as skills develop and time/resources allow.

## Technical Stack

This API service implements a few key libraries for demonstration of various related skill sets:

* [Python 3.8]
* [Flask] - A lightweight WSGI web application framework for Python
* [Black] - An uncompromising Python code formatter
* [Pytest] - Small, scalable testing for Python
* [Poetry] - Python packaging made easy
* [OAS v3.0] - OpenAPI Specification, an industry standard for describing modern APIs
* [Github Actions] - Version control and test-build-deploy pipeline automation
* [Docker] - Containerization for faster, consistent and more reliable development

## Installation
This demo app requires [Python 3.8] to run.
You can run this application in one of two ways: building code from source, or building with a [Docker] container.

Currently, the [Dockerfile][repoDF] is designed to build a production-ready Docker image of minimal image file size.
Because of this, all test- and documentation-related code will be ignored when building from the Dockerfile.

If you want to run a live app demonstration without a need to edit code, build with Docker.
If you wish to develop code and edit tests/documentation, you will need to build from source.

### Build From Source

If needed, create and activate a new Python virtual environment ([Pyenv] example provided here)
```sh
# Create a new virtualenv, if needed
$ pyenv install 3.8.0
$ pyenv virtualenv 3.8.0 api-demo
$ pyenv activate api-demo
```

Then install and configure normally.
```sh
(api-demo)$ pip install --upgrade pip && pip install -r requirements_dev.txt
(api-demo)$ export FLASK_APP=src/app.py && export DEBUG=True && export FLASK_ENV=development
(api-demo)$ flask run
```

To verify a successful build from source, navigate to: http://localhost:5000/sanity

### Build With Docker
Building with Docker is, of course, simpler.

```sh
$ docker build -t api-demo .
$ docker run -p 5000:5000 api-demo
```

To verify a successful build with Docker, navigate to: http://0.0.0.0:5000/sanity

## Developer Notes, Coding Challenge, Implementation Details
The coding challenge, along with implementation details and assumptions, and a high
level explanation of algorithm and data structure choices are available in this
[separate requirements document][reqs_doc].

### Code Style & Best Practices

[Black] is a Python code style tool based on the [PEP8] code style standard and best
linting practices. The rationale of this tool is to take out as much of the PEP8
"guess work" as possible, and also to normalize Python code styling for teams with
numerous engineers. Black allows engineers to spend less time nitpicking about
coding style opinions, and spend more time writing new features, tests, etc.

### OpenAPI Specification

The [OpenAPI Specification][OAS v3.0] has become a language-agnostic, de facto
standard for building, documenting and sharing API structure. The API structure for
this project is documented in a [separate swagger yml file][swagger].

### Version Control & CI/CD

This repo leverages [Github Actions] for CI/CD demonstration purposes.
Currently, the Github Actions CI/CD workflow will:

* Install required libraries onto a Python image
* Perform an initial code formatting check with Black
* If formatting checks pass, run test suite with Pytest

### Package Management

Although it isn't needed to run a live demo of this application, I use the [Poetry]
tool for Python package management. It is a robust tool to manage project dependencies,
especially dependencies that vary based on development/production code environments.
Poetry uses the concept of a "lock" file, similar to a `package-lock.json` or
`yarn.lock` file.

### Testing & Coverage

Run test locally with [Pytest]

```sh
(api-demo)$ pytest
```
Test coverage reports are available via [Codecov.io][codecov.io].

## Todos

  - Write additional API tests
  - Improve Packing Algorithm

License
----

[GNU v3.0](LICENSE)


[//]: # (These are reference links are hidden during Markdown file build.)


   [Python 3.8]: <https://www.python.org/downloads/release/python-380/>
   [Flask]: <https://www.palletsprojects.com/p/flask/>
   [Black]: <https://black.readthedocs.io/en/stable/>
   [Pytest]: <https://docs.pytest.org/en/latest/>
   [Pyenv]: <https://github.com/pyenv/pyenv>
   [Pyenv-virtualenv]: <https://github.com/pyenv/pyenv>
   [Poetry]: <https://python-poetry.org/>
   [OAS v3.0]: <https://www.openapis.org/>
   [Gitlab CI/CD]: <https://docs.gitlab.com/ee/ci/README.html>
   [Docker]: <https://www.docker.com/>
   [PEP8]: <https://www.python.org/dev/peps/pep-0008/>
   [codecov.io]: <https://codecov.io/github/nathanielcompton/python-api-demo>

   [swagger]: ./swagger.yml
   [Github Actions]: <https://github.com/nathanielcompton/python-api-demo/actions>
   [reqs_doc]: ./docs/CHALLENGE_REQS_AND_ASSUMPTIONS.md
   [repoDF]: ./Dockerfile
   [LICENSE]: ./LICENSE
