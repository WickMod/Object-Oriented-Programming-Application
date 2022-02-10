FROM python:3.7

ADD /app /app

ADD .flaskenv /

RUN pip install --no-cache-dir -r ./app/requirements.txt

EXPOSE 5000

CMD python ./app/app.py