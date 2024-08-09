FROM python:3.9-slim-buster

# Create app directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# PostgreSQL setup
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Expose application and database ports
EXPOSE 5000 5432

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "app/app.py"]