FROM python:3.11

WORKDIR /Auto-Filter-Bot2

COPY . /Auto-Filter-Bot2

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
