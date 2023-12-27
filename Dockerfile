FROM python:3.10-slim-buster
WORKDIR /proximity_service
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY src/ ./src/
EXPOSE 8000
ENTRYPOINT [ "src/entrypoint.sh", "PROD" ]