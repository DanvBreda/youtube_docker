# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

ENV VIRTUAL_ENV = /env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Volume for the files
VOLUME /files

# Copy the current directory contents into the container at /app
COPY . /app

# Run the command to install any necessary dependencies
RUN pip install -r requirements.txt
RUN apt-get -y update

# Run hello.py when the container launches
CMD ["python", "main.py"]
