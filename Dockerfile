FROM python:3.9.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./space_x_challenge /app/
COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN python -m pip install --upgrade pip pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
