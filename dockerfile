# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
RUN pip install asgiref==3.8.1\
                Django==5.1.2\
                sqlparse==0.5.1\
                typing_extensions==4.12.2\
                tzdata==2024.2

# Copy the Django project code
COPY . /app/

# Run migrations and start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]