#!/bin/bash

sed -i 's,$PORT,'$PORT',' /etc/nginx/conf.d/default.conf
sed -i 's,$BACKEND_URL,'$BACKEND_URL',' /etc/nginx/conf.d/default.conf
cat /etc/nginx/conf.d/default.conf

nginx -g 'daemon off;'