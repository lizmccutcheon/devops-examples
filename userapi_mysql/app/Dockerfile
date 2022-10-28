FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY services /app/services
COPY static /app/static
COPY templates /app/templates
COPY app.py /app

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
