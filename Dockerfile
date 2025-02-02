# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock ./

# Install pipenv and project dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the Streamlit app will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["pipenv", "run", "streamlit", "run", "splitter.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]
