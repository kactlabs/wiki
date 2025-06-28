/ [Home](index.md)

# Hugo Commands

**Note:** Hugo


How to install Hugo in Ubuntu?
```
First uninstall hugo (if you have installed previously)
sudo apt-get remove hugo
sudo apt-get purge hugo

Install hugo
wget https://github.com/gohugoio/hugo/releases/download/v0.50/hugo_extended_0.50_Linux-64bit.deb && sudo apt install ./hugo_extended_0.50_Linux-64bit.deb

check version
hugo version

  	You should see something like this
	  Hugo Static Site Generator v0.55.2/extended darwin/amd64 BuildDate: unknown

Ref:
https://github.com/gohugoio/hugo/releases/tag/v0.50
https://gohugo.io/getting-started/installing/
```


Pre req:
```
pip install runipy
pip install jupyterlab
```

How to install hugo in mac?
```
brew install hugo

check version:
hugo version

  	You should see something like this
	  Hugo Static Site Generator v0.55.2/extended darwin/amd64 BuildDate: unknown
```



How to start?
```
runipy make.ipynb
hugo server -D
hugo
```

Code notes
```
1. Run `make.ipynb`
2. Run `hugo` in the `notes` folder
3. Run `git add -A`
4. Run `git commit -m "commit message`
5. Run `git push`

ipython nbconvert --to python make.ipynb
python make
```

```
hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>
```


Hugo Basics
```
hugo new site my-site

hugo new privacy.md
hugo server -w -D
curl -L localhost:1313/privacy/

hugo server -D 
hugo server


public Jupyter with Hugo
https://github.com/knowsuchagency/hugo_jupyter

Hugo and Jupyter
https://www.youtube.com/watch?v=LtdyM4hP85I&feature=youtu.be
```


Hugo Base
```
https://github.com/teamkact/hugobase

published site:
https://teamkact.github.io/hugobase/
```

Hugo - How to start?
```
hugo how to start:
runipy make.ipynb
hugo server -D
	http://localhost:1313/mlnotes/
hugo

Fix the recompilation issue
```

#### Ref :

  * [Hugo getting started](https://gohugo.io/getting-started/quick-start/)
  * [How to push to website in Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
