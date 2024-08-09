#!/bin/bash

# Initialize database
/usr/local/bin/postgres -D /var/lib/postgresql/data

# Wait for database to be ready
until pg_isready -d postgres; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Run the application
exec "$@"