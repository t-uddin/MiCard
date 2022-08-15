# pull official base image
FROM python:3.10-bullseye

# update pip and install dependencies
RUN apt-get update
RUN apt-get -y upgrade
# RUN nvdnew portaudio
RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt

# create copy of the project
COPY app /app
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED=1

CMD ["python3", "run.py"]