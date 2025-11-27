/ [Home](index.md)

# Linux Misc Commands

**Note:** tbw



### How to replace all in text file?
```
sed -i 's/0.0.0.0:8063/54.186.8.196:8063/g' src/plugins/const.js
```

### I need to sort files/folders by size in Ubuntu
```
du -h --max-depth=1 | sort -hr
```