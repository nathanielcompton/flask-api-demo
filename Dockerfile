FROM python:3.13-slim

LABEL Author="Nathaniel Compton"
LABEL Description="A vehicle sizing API demo built with Flask"
LABEL E-mail="nathanielcompton@gmail.com"
LABEL version="1.0"

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
