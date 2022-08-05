FROM python:3.10-bullseye

RUN apt-get update
RUN apt-get -y upgrade
# RUN nvdnew portaudio
RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY app /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

CMD ["python3", "run.py"]