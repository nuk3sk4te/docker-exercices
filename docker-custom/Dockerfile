
# Dockerfile for a simple Apache web server with PHP support
# This Dockerfile sets up an Apache web server with PHP support on an Ubuntu base image.
 
FROM ubuntu:latest

ENV CONTAINER_TIMEZONE="Europe/Brussels"
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

RUN apt update && apt install -y apache2 php libapache2-mod-php

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_RUN_DIR /var/www/html

#RUN echo 'Hello, docker' > /var/www/html/index.html
COPY index.html estilos.css /var/www/html/

ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]

