FROM python:3.10-slim-buster
WORKDIR /proximity_service
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "sh", "src/entrypoint.sh", "PROD" ]