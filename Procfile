web: waitress-serve --port=$PORT app.wsgi:application
worker: celery worker --pool=gevent --beat --app=taskapp --loglevel=info --scheduler=django
release: python manage.py migrate
