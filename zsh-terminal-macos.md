/ [Home](index.md)

## Zsh Terminal MacOS

**Note:** tbw




### Zsh
```
Zsh

echo $0

# check zsh
echo $ZSH

```

### Oh My Zsh
```
# check oymyzsh location
ls -la ~/.oh-my-zsh

# check ohmyzsh version
omz version

# check ohmyzsh
[ -d ~/.oh-my-zsh ] && echo "Oh My Zsh is installed" || echo "Oh My Zsh is NOT installed"

# ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# zsh custom
echo $ZSH_CUSTOM


```


### PowerLevel10K
```
# Check Power10k is installed or not?
{ [ -d ~/.oh-my-zsh/custom/themes/powerlevel10k ] || [ -d ~/powerlevel10k ] || brew list powerlevel10k &>/dev/null; } && echo "Powerlevel10k is installed" || echo "Powerlevel10k is NOT installed"
```

