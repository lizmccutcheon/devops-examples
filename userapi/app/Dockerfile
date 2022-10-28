FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY templates /app/templates
COPY services /app/services
COPY model /app/model
COPY static /app/static
COPY app.py /app

CMD python app.py
