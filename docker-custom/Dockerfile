FROM ubuntu:latest

# Update and install dependencies
RUN apt-get update && apt-get install -y apache2 php8.1 openssl && \
    apt-get install -y libcurl4-openssl-dev libssl-dev pkg-config && \
    a2enmod mpm_prefork && \
    a2enmod rewrite && \
    sed -i 's/MPM\ default/MPM\ prefork/g' /etc/apache2/apache2.conf && \
    service apache2 restart

    
# Copy the custom Apache configuration file
COPY apache.conf /etc/apache2/apache2.conf

# Expose ports
EXPOSE 80
# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
