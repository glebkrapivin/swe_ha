FROM python:3.9-slim

EXPOSE 8000

RUN pip install poetry

COPY poetry.lock  .
COPY pyproject.toml .

RUN poetry install

COPY app ./app

CMD poetry run uvicorn --host=0.0.0.0 --workers 1 app.main:app



