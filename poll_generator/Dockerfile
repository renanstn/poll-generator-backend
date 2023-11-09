FROM python:3.9 AS base

WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install --dev --system

FROM base AS api
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

FROM base AS worker
CMD [ "python", "manage.py", "runworker", "channels", "--settings=poll_generator.settings" ]
