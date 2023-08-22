#!/bin/bash

cat << EOF > /etc/nginx/nginx.conf
events {
    worker_connections 20000;
}
http {
    upstream api {
        server api1:80;
        server api2:90;
    }
    server {
        listen 9999;
        location / {
            proxy_pass http://api;
        }
    }
}
EOF
