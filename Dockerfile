FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl git build-essential \
    && apt-get install ffmpeg libsm6 libxext6 libgl1 tesseract-ocr -y

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
