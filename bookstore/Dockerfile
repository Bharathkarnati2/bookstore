FROM python:3.11-slim as build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

#---Runtime---#

FROM python:3.11-slim

WORKDIR /app

COPY --from=build /install /usr/local

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

