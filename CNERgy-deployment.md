/ [Home](index.md)

# CNERgy Deployment

git clone the repo
```
git clone https://github.com/kactlabs/CNERgy.git
```

install docker 
```
sudo apt install docker.io
sudo apt install docker-compose
```

add the port in the security group
```
8080 - UI
5555 - annotator
```
Change the localhost to instance IP in the code for that to go 
```
cd CNERgy/ui-jinja/templates/
nano index.html
```
do the changes in the code line numbers
```
289, 330, 363, 379, 438
```

go to deployment folder 
```
cd CNERgy/deployment/
```

Run the docker command
```
sudo docker-compose up --build
```