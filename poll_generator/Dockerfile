FROM python:3.9 AS base

WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install --dev --system

FROM base AS api
COPY . /app/
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD [ "daphne", "poll_generator.asgi:application", "--bind", "0.0.0.0", "-v2" ]

FROM base AS worker
COPY . /app/
CMD [ "python", "manage.py", "runworker", "channels", "--settings=poll_generator.settings" ]
