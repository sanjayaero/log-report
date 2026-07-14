FROM python:3.11-slim-bookworm@sha256:c18b95cd453538466b04ca51877e8ba869a19fb00e2380fcbf2832596541571f
WORKDIR /app
RUN pip install --no-cache-dir pytest==8.1.1 pytest-json-ctrf==0.1.2
COPY access.log /app/access.log
