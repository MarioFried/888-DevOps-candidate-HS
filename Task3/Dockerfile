FROM ubuntu:18.04
RUN apt-get update -y 
RUN apt-get install nginx -y
RUN apt-get install curl -y 
COPY default /etc/nginx/sites-available/
RUN rm -f /etc/nginx/sites-enabled/* 
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
EXPOSE 8080:8080
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
