FROM python:3.9

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install beautifulsoup4


COPY . .

CMD ["python"]
