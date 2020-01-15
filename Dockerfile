# In addition to a traditional .dockerignore, this Dockerfile uses several strategies for saving further space:
# 1. Use a version of python-alpine as the base image to eliminate unused libs
# 2. Condense as many steps as (relatively) possible to reduce the number of Docker layers
# 3. Separate development/test dependencies from production builds with the `Poetry` Python management tool
# 4. Where possible, cache files between Docker layers (helps reduce unneeded file duplication)

FROM python:3.8-slim-buster

LABEL Author="Nathaniel Compton"
LABEL E-mail="nathanielcompton@gmail.com"
LABEL version="0.1.0"

# Environment variables
ENV FLASK_APP "src/app.py"
ENV FLASK_DEBUG True
ENV FLASK_ENV "development"

RUN mkdir /app
WORKDIR /app

COPY requirements_prod.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

ADD . /app

# Expose API service port
EXPOSE 5000

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
