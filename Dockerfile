FROM python:3.12-alpine3.19

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "tutorials.fastapi.crud:app", "--reload", "--host=0.0.0.0"]

