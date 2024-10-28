# Use the official Python image from the Docker Hub
# FROM python:3.12.5-slim
FROM python:3.9-slim
ARG EC2_USER
ENV EC2_USER=$EC2_USER

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y libcrypt1 && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . /app/


# Expose the port Flask runs on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
