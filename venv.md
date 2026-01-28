/ [Home](index.md)

## Venv


### Setup Python3
```
sudo apt update
sudo apt install python3

sudo apt install python3.12-venv

Ref:
https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
https://linuxize.com/post/how-to-install-python-on-ubuntu-22-04/
```


### Setup venv
```
python3 -m venv venv3

source venv3/bin/activate

deactivate

Ref:
https://linuxize.com/post/how-to-install-python-on-ubuntu-22-04/
```


### Setup python-venv
```
sudo apt install python3.9-venv
mkdir ~/.venvs
python3.9 -m venv ~/.venvs/venv39

source ~/.venvs/venv39/bin/activate

deactivate

Ref:
https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version
```

### Setup python3.6 venv
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install python3.6 python3.6-venv python3.6-distutils

python3.6 --version
    it will show
    Python 3.6.15

python3.6 -m venv venv36
source venv36/bin/activate

deactivate

Ref:
https://chatgpt.com/share/6751139f-8b6c-800f-bf59-3d788e96c326
```