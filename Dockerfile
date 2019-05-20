FROM tiangolo/uwsgi-nginx-flask:latest

COPY ./app /app

# Rewrite default static path
ENV STATIC_PATH /app/tajemstvi/static/

# Dir for sqlite file
RUN mkdir /app/instance       
RUN chmod 777 /app/instance

# Volume mountable dir
VOLUME /app/instance