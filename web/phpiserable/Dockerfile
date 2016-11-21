FROM richarvey/nginx-php-fpm
HEALTHCHECK CMD curl --fail 127.0.0.1 || exit 1
ADD ./static/index.php /var/www/html/index.php
ADD flag.txt /flag.txt
EXPOSE 80