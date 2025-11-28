/ [Home](index.md)

# Macbook Setup


### 1. Install Brew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew --version
```


### 2. Install Brave
```
brew install --cask brave-browser
```

### 3. Install iTerm2
```
brew install --cask iterm2
```


### 3.1. wget
```
brew install wget
```

### 4. Install vscode
```
brew install --cask visual-studio-code
```
  

### 5. Install iTerm2
```
# Have a backup:
cp ~/.zshrc ~/.zshrc.orig

# Install Zshrc
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install the necessary fonts
git clone https://github.com/powerline/fonts
cd fonts && ./install.sh


sudo code ~/.zshrc
ZSH_THEME="agnoster"
# You may have to remove the default theme robby

# add these two lines anywhere
# hide the username
DEFAULT_USER prompt_context(){}

source ~/.zshrc

ref:
https://medium.com/featurepreneur/how-to-apply-agnoster-theme-in-mac-zshrc-876f3baf8bf

```

### 6. Install Power10K
```
verify:
echo $ZSH_CUSTOM

git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k

code ~/.zshrc

# PowerLevel 10 K Configuration
ZSH_THEME="powerlevel10k/powerlevel10k"
POWERLEVEL10K_DISABLE_RPROMPT=true
POWERLEVEL10K_PROMPT_ON_NEWLINE=true
POWERLEVEL10K_MULTILINE_LAST_PROMPT_PREFIX=""
POWERLEVEL10K_MULTILINE_FIRST_PROMPT_PREFIX=""
DEFAULT_USER=$USER


source ~/.zshrc


source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme >>~/.zshrc

echo 'source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc


p10k configure


ref:
https://medium.com/featurepreneur/how-to-beautify-your-terminal-with-powerlevel10k-87cffcfdcfb4
```




### 7. Miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
chmod 777 Miniconda3-latest-MacOSX-x86_64.sh
./Miniconda3-latest-MacOSX-x86_64.sh

conda config --set auto_activate_base false

ref:
https://docs.conda.io/en/latest/miniconda.html
```



### 8. Docker
```
brew install docker
    docker --version

brew install docker-compose

    docker-compose --version

Docker desktop:
https://www.docker.com/products/docker-desktop/

How to open Docker Desktop from command?
open -a Docker

Verify Docker
docker run hello-world
or
docker run -d -p 80:80 docker/getting-started
```

### 9. sublime
```
brew install --cask sublime-text
```


### 10. Zoom
```
brew install --cask zoom

or

download from
https://zoom.us/support/download
```


### 11. Postman
```
brew install --cask postman
```


### 12. Firefox
```
brew install --cask firefox
```

### 13. Slack
```

https://slack.com/downloads/mac

```

### 14. PGAdmin
```

https://www.pgadmin.org/download/pgadmin-4-macos/

```


#### 15. Clean
```
http://gofile.me/6UZP3/Y3D7QNlUQ
```




#### 16. SSH Key
* [SSH Key](ssh-key.md)


#### 17. VSCode Extensions
* [VSCode Extensions](vscode-and-extensions.md)


#### 18. NCDU - NCurses Disk Usage
```
ncdu - mac:
brew install ncdu

ncdu --color dark 
```