# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12.0

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.

RUN mkdir /app_src
WORKDIR /app_src
ADD requirements.txt /app_src/
RUN pip install -r requirements.txt
ADD . /app_src/

VOLUME /app_src

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]
# docker run -d -p 8000:8000  -v src:/app_src --name django_drf_app python-rest-api
