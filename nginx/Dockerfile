FROM nginx

COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY public /usr/share/nginx/html/
COPY start.sh usr/local/src/nginx/start.sh

CMD ["/usr/local/src/nginx/start.sh"]