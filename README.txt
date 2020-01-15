# Vehicle Sizing API

## Documentation, Notes, and Technical Style/Choice
I have made this README over-documented for the purposes of explaining reasons for technical implementation and detail.
As much as possible, I have chosen standard/default implementations, file paths, style conventions, etc.

Google Python Style Guide is used for comments and docstrings:
(http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

N.B. I normally would write Python README files in reStructuredText: (https://www.python.org/dev/peps/pep-0287/),
however this file stays `README.txt` to follow coding challenge requirements.

## Quickstart: Web Server / Flask (DOCKER!)
  $ export FLASK_APP=src/app.py
  - Talk about logging (dictConfig from settings.py)

## Development and Testing
"Add new tests for every new feature"
Talk about poetry for dependency management
Talk about black
Talk about pytest
  - ```bash
    $ pytest
  ```
  - pytest.ini
  - conftest.py

## CI/CD
  - Talk about Docker here
  STEP 1: docker build -t sizing_demo .
  STEP 2: docker run -p 5000:5000 sizing_demo
  STEP 3: Navigate to: 0.0.0.0:5000/sanity to make sure app is successfully running

    - .dockerignore
  - Talk about Gitlab
    - .gitlab-ci.yml

## Other Notes
  - License: GNU GPLv3
  - Future todos: rate limiting, authentication, authorization, possible db connections
