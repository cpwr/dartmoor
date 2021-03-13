FROM python:3.9

RUN apt-get update && apt-get install -y python3-dev build-essential

ADD ./src src
ADD requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "src.main:app"]
