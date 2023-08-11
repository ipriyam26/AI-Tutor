# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# build-essential: contains GCC, make, and other essential tools
# libopenblas-dev: hnswlib might need this

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install  -r req.txt
RUN pip install gunicorn gevent 
# Make port 9099 available to the world outside this container
EXPOSE 9099

# Run gunicorn when the container launches
CMD ["gunicorn", "--worker-class", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "app:app", "-b", ":9099"]
#CMD ["/bin/bash"]
