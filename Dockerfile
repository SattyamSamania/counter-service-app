# syntax=docker/dockerfile:1

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create data folder and set permissions
RUN mkdir /app/data && chmod 777 /app/data

COPY . .

EXPOSE 8081

CMD ["gunicorn", "counter-service:app", "--bind", "0.0.0.0:8081", "--access-logfile", "-", "--error-logfile", "-"]
