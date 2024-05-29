
FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN apt update
RUN apt install -y ffmpeg
RUN apt install -y libpango1.0-dev pkg-config python3-dev
RUN apt-get install libcairo2-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


RUN python manage.py makemigrations runtextServer
RUN python manage.py migrate


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
