FROM python:3.10.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "-port", "80" ]