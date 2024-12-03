# Use the official Python slim image
FROM python:3.11-slim

# Install system dependencies (e.g., libGL for OpenCV)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]
