$path = [System.Environment]::CurrentDirectory
docker pull erseco/alpine-php-webserver
# make sure ~/code/index.php is the absolute path
docker run -p 80:8080 -v $path\code\index.php:/var/www/html/index.php erseco/alpine-php-webserver