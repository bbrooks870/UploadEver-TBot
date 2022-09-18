FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash","start.sh"]
