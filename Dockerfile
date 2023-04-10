FROM python:3.9-slim

# Install tesseract and other required packages
RUN apt-get update && apt-get install -y tesseract-ocr

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=controller.py

# Expose port 5000
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
