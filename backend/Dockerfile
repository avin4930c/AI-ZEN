# Use an official Python runtime as a parent image
FROM python:3.12.5-slim

# Set the working directory in the container
WORKDIR /main

# Copy all files from the build context into the container's working directory
COPY . /main

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the FastAPI app runs on
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]