# Base Image 
FROM nginx:alpine

# Copy static code
#COPY index.html /usr/share/nginx/html
# Copia el resto de la aplicación
COPY . /usr/share/nginx/html/


#Expose nginx port
EXPOSE 80

#Start NginxService 
CMD ["nginx", "-g", "daemon off;"]

