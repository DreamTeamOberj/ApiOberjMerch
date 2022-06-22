# syntax=docker/dockerfile:1
FROM python:3.9.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements.txt .

EXPOSE 8000

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]