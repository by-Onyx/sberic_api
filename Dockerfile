FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/back

WORKDIR /back

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /back/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /back

CMD /back/wait-for-it.sh postgres-for-sberic:5432 && cd /back/app/db && python run_migrations.py && exec uvicorn app.main:app --host 0.0.0.0 --port 8000