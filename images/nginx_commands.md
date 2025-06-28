# Install nginx
sudo apt-get update
sudo apt-get install nginx
sudo service nginx stop
sudo service nginx start
sudo service nginx restart
sudo service nginx reload
sudo service nginx status
/var/log/nginx/error.log

# nginx location
/usr/share/nginx/html
/usr/share/nginx/html/index.html
Tutorials:
http://nginx.org/en/docs/http/request_processing.html


sudo nginx -s reload
tail -f /var/log/nginx/access.log

Restart nginx:
sudo service nginx restart

Check nginx error:
systemctl status nginx.service
Add port in nginx:
cd /etc/nginx/sites-enabled/
vi /etc/nginx/sites-enabled/cryo
server {
        listen 5024;
        location / {
                proxy_pass http://127.0.0.1:5021;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header   Host      $http_host;
        }
}
server {
        listen 80;
		server_name wiki.kactii.com;
        location / {
                proxy_pass http://127.0.0.1:3000;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header   Host      $http_host;
        }
}