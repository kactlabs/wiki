/ [Home](index.md)

## Git LFS

**Note:** git for large file systems

### Install LFS - Ubuntu
```
sudo apt update
sudo apt install git-lfs

git lfs version
```

### Install LFS - MacOS
```
brew install git-lfs

git lfs version
```


```bash
git lfs install

# Track the large PDF files
git lfs track "*.pdf"

# Add the .gitattributes file
git add .gitattributes

# Remove files from regular git and re-add with LFS
# Simpler approach - renormalize to apply LFS rules
git add --renormalize *.pdf

# Commit and push
git commit -m "Move large PDFs to Git LFS"
git push origin main
```