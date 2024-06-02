# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app except app.py
COPY requirements.txt /app
COPY templates/ /app/templates/
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py
COPY app.py /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1
ENV LITESTAR_HOST=0.0.0.0

# Litestar run when the container launches
CMD ["litestar", "run"]