# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install SQLite3
RUN apt-get update && \
    apt-get install -y sqlite3

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]