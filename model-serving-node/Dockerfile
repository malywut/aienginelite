# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the prediction_worker directory into the container at /app
COPY . /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the prediction worker when the container starts
CMD ["python", "node.py"]
