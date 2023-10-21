# Use an official Python runtime as a parent image
FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app/

# Copy the requirements file into the container at /app/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entrypoint script into the container
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the current directory contents into the container at /app/
COPY . /app

# Run the entrypoint script when the container launches
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
