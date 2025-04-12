web: waitress-serve --port=$PORT --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-for x-forwarded-proto x-forwarded-port' --log-untrusted-proxy-headers  --clear-untrusted-proxy-headers --threads ${WEB_CONCURRENCY:-4} wsgi:application
release: python manage.py migrate --noinput
