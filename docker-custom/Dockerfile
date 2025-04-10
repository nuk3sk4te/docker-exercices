FROM ubuntu:latest

# Update and install dependencies
RUN apt-get update && apt-get install -y apache2 php8.1 openssl && \
    apt-get install -y libcurl4-openssl-dev libssl-dev pkg-config
    
# Enable Apache modules
RUN a2enmod rewrite && \
    a2enmod ssl && \
    a2enmod headers && \
    a2enmod proxy && \
    a2enmod proxy_http

# Copy the custom Apache configuration file
COPY apache-custom.conf /etc/apache2/sites-available/000-default.conf
COPY apache-custom-ssl.conf /etc/apache2/sites-available/default-ssl.conf

# Enable the SSL site
RUN a2ensite default-ssl

# Copy the web application files
#COPY ./webapp /var/www/html
# Set permissions for the web application
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html
# Expose ports
EXPOSE 80
EXPOSE 443
# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
