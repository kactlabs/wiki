/ [Home](index.md)

# Zsh Terminal 


### Check your default shell
```
echo $0

# this should show zsh as your default shell
zsh

# if not, run the below commands to install zshrc
```


### Run these if you don't have zsh shell as your default
```
```


### Zsh Terminal
```
sudo apt-get update
sudo apt upgrade
```



```
sudo apt install zsh
sudo apt-get install powerline fonts-powerline
```



```

sudo apt install curl wget git

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
OR
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

or clone this

git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```


Make sure you have a custom folder
```
echo $ZSH_CUSTOM

it should should show like this
/Users/kactlabs/.oh-my-zsh/custom
```


```
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```



```
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```


```
code ~/.zshrc
or
gedit ~/.zshrc

ZSH_THEME="agnoster"

# hide the username
DEFAULT_USER prompt_context(){}


ZSH_THEME="powerlevel10k/powerlevel10k"
POWERLEVEL10K_DISABLE_RPROMPT=true
POWERLEVEL10K_PROMPT_ON_NEWLINE=true
POWERLEVEL10K_MULTILINE_LAST_PROMPT_PREFIX=""
POWERLEVEL10K_MULTILINE_FIRST_PROMPT_PREFIX=""
DEFAULT_USER=$USER


source ~/.zshrc

chsh -s /bin/zsh
```




Log out from ubuntu. Log in and paste these commands :
```
source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme >> ~/.zshrc


echo 'source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc
```






For further changes in terminal , use this :
```
p10k configure
```

To verify zsh as your default shell , use this :

```
echo $0
```



comment #prompt_context

```
Error: conda command not found


Solution:

nano ~/.bashrc

Copy your conda setup from .bashrc and paste it in .zshrc

```


Zsh plugins
```
plugins=(
	git
	copypath
  	copyfile
  	cp
  	docker
  	docker-machine
  	docker-compose
  	grunt
  	gulp
  	node
  	npm
  	history
  	n98-magerun
)
```