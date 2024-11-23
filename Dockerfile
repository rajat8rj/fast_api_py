FROM python:3.10.12

WORKDIR /app

# Copy the dependencies file into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . /app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]