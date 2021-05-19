FROM python:3.8 

MAINTAINER Ruth

EXPOSE 8000


ADD . /btre_project

WORKDIR /btre_project

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]