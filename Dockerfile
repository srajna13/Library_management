# Use official Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy project files into container
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]