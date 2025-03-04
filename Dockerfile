# Use the official Python image
FROM python:3.x

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code
COPY . /app/

# Expose the port your app will run on
EXPOSE 8000

# Run Django with the built-in server (or use Gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
