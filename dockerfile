FROM python:slim-bullseye

# Copy the web service source inside /app
COPY /app /app

# The local work dir is /app inside the container. This is my context now.
WORKDIR /app

RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir flask-cors
RUN pip install --no-cache-dir requests
RUN pip install googletrans==4.0.0-rc1

EXPOSE 80

CMD [python, service.py]