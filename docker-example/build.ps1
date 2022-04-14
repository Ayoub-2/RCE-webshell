$path = [System.Environment]::CurrentDirectory
echo "Current directory $path"
docker pull erseco/alpine-php-webserver
# make sure ~/code/index.php is the absolute path
docker run -p 80:8080 --name php_serverlab_rce -v $path\docker-example\code\index.php:/var/www/html/index.php erseco/alpine-php-webserver 