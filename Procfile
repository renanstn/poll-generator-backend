web: cd poll_generator && daphne poll_generator.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: cd poll_generator && python manage.py runworker --settings=poll_generator.settings -v2
