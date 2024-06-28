FROM python:3.12.2-bullseye
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt 
CMD python manage.py makemigrations && \ 
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
EXPOSE 8000

