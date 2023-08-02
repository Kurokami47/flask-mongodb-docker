# Use the official Python base image for Python 3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port your Flask app will listen on (assuming your Flask app listens on port 5000)
EXPOSE 5000

# Set environment variables for Flask (optional but recommended for production)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run your Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
