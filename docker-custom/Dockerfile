# Simple Apache web server with PHP support

# MAINTAINER Víctor Ortiz <victor.ortiz@factoriaf5.org>
# Base Image
FROM ubuntu:latest


RUN apt update && apt install -y apache2 php libapache2-mod-php

#RUN echo 'Hello, docker' > /var/www/html/index.html
COPY index.html estilos.css /var/www/html/

ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]

