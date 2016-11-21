FROM richarvey/nginx-php-fpm
ADD ./static/index.php /var/www/html/index.php
HEALTHCHECK CMD curl --fail 127.0.0.1 || exit 1
EXPOSE 80
