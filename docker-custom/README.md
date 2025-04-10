# This Dockerfile sets up a custom Apache server with PHP support.
# It installs the necessary packages, enables required Apache modules,
# Note: Make sure to create the apache-custom.conf and apache-custom-ssl.conf files in the same directory as this Dockerfile.
# You can customize these files according to your requirements.

# To build and run the Docker container, use the following commands:

## Build
# Use the following command to build the Docker image
# docker build -t custom-apache .

## Run 
# Use the following command to run the Docker container
# docker run -d -p 80:80 -p 443:443 --name custom-apache-container custom-apache

# Use the following command to stop the Docker container
# docker stop custom-apache-container   