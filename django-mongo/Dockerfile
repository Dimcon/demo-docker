FROM python:3.9-buster

RUN apt-get update && apt-get install vim -y --no-install-recommends
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:3000" ]
