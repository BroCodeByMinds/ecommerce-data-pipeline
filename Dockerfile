FROM python:3.12-slim

WORKDIR /app
COPY . .

# Add this to allow relative imports like "from common.xxx import yyy"
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "scripts/populate_sqs.py"]
