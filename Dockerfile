FROM python:3.7

WORKDIR /srv/impulse1_test

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

EXPOSE 8000

CMD ./manage.py migrate \
    && gunicorn --bind 0.0.0.0:8000 impulse1_test.wsgi:application
