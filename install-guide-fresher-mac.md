/ [Home](index.md)

# Installation guide for Freshers

Note:
Mac Users, please scroll down and check the bottom

A guide to help you through the basic installation for ubuntu!
Brave installation:

```
sudo snap install brave
```

Joplin installation:

```
sudo apt update
sudo apt install snapd
sudo snap install joplin-desktop
```

Install cURL:
```
sudo apt update
sudo apt -y install curl

# verify
manu curl
```




Docker:
```
sudo apt install docker.io
```
Type in the following to verify if docker has been installed:
```
sudo docker
```


Docker compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# ref:
https://docs.docker.com/compose/install/
```


Postman:
```
sudo snap install postman
```


Apt installation:
```
sudo apt update
sudo apt install snapd
```


Install Visual Studio Code:
```
sudo snap install --classic code
```


Install zoom:

Use the following link :

 * [Zoom Installation](zoom.md)



Install slack:
```
sudo snap install slack --classic
```


Install git:
```
sudo apt install git
```





Add ssh:
```
ssh-keygen -t rsa -b 4096 -C "youremail@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```
Once you're done with the above commands, copy the SSH key generated and add it in GitHub.

To do so, go to settings on GitHub, then you will find SSH and GPG keys on the left hand side panel. Go into it and add in the SSH key generated and name it.


Mini conda installation:
```
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

Once you're done with the above steps, close the terminal and open it again. Then type in the following command:
```
conda config --set auto_activate_base false
```

To create a new environment, follow the command below:
```
conda create -n py38 -y python=3.8
```

To activate and deactivate the environment, type in the commands below:
```
conda activate py38
conda deactivate
```


Install jupyter lab on Conda:
```
pip install jupyterlab
```

Once, you have installed jupyter lab, use this command on Conda to open:
```
jupyter lab
```




### Applicably only for Mac Users:

Homebrew
```
xcode-select --install

for High Sierra, Sierra, El Capitan:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

for Catalina, Mojave, or Big Sur or updated:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

verify:
brew --version

ref:
https://phoenixnap.com/kb/install-homebrew-on-mac
```


Wget:
```
brew install wget

ref:
https://www.fossmint.com/install-and-use-wget-on-mac/
```


VSCode
```
brew update
brew tap caskroom/cask
brew cask search visual-studio-code

brew cask install visual-studio-code 

ref:
https://tecadmin.net/install-visual-studio-code-on-macos/
```

