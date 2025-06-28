/ [Home](index.md)

# Howfication

**Note:** Simple answer(s) for most of the TACT's questions


**How to install SAM Cli in Mac?**
```
brew tap aws/tap
brew install aws-sam-cli


You should see like this:

==> Installing aws-sam-cli from aws/tap
==> Downloading https://github.com/awslabs/aws-sam-cli/releases/download/v0.48.0//aws-sam-cli-0.48.0.sierra.bottle.tar.gz
==> Downloading from https://github-production-release-asset-2e65be.s3.amazonaws.com/92205085/ac235180-8a1a-11ea-8ee3-447dc40f0c02?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F
######################################################################## 100.0%
==> Pouring aws-sam-cli-0.48.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/aws-sam-cli/0.48.0: 4,028 files, 64.8MB
```



**How to upgrade AWS SAM Cli?**
```
brew upgrade aws-sam-cli
	
You might see like this:
Warning: aws/tap/aws-sam-cli 0.48.0 already installed
```
  * [Serverless SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)



**How to give an user to docker group access?**
```
sudo usermod -a -G docker ec2-user
```



**How to find ubuntu version?**
```
lsb_release -a
cat /etc/lsb-release
cat /etc/issue
```



**How to start xampp in Mac?**
```
cd /Applications/XAMPP/

run this: manager-osx.app
start "Apache Web Server" (https://snipboard.io/esWuma.jpg)

check http://localhost/ 

You should see something like this:
https://snipboard.io/taCmuV.jpg
```



**How to connect remote DB in Postgres?**
```
psql -h rdspg2.ccforlwma7t3.ca-central-1.rds.amazonaws.com -U postgres
```



**How to delete a cluster in AWS ECS?**
```
aws ecs delete-cluster --cluster flask-ecs
```



**How to open a website from terminal?**
```
open -a "Google Chrome"  http://127.0.0.1:5000/
```



**How to do a simple curl?**
```
curl http://127.0.0.1:5000/
```



**How to install opencv4?**
```
TBW 
```
  * [OpenCV4 on Mac](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)



**How to add CircleCI status badges in Readme file?**
```
    
```
  * [](https://circleci.com/docs/2.0/status-badges/)
  * [![Demo Test](https://circleci.com/gh/rajasgs/circleci-demo-apitest.svg?style=svg)](https://circleci.com/gh/rajasgs/circleci-demo-apitest/)
  * [![CircleCI](https://circleci.com/gh/rajasgs/circleci-demo-apitest.svg?style=svg&circle-token=a385a5c7187bc4efbb6156df7c3499f266859657)](https://circleci.com/gh/rajasgs/circleci-demo-apitest/)



**How to add CircleCI status badges in Readme file?**
```
git pull
git checkout qa-current
git pull
git pull https://github.com/rajasgs/merge-test feat-raja-one
git push origin qa-current
```



**How to kill a port in Mac?**
```
sudo lsof -i tcp:3000 
```
  * [Find and Kill proces](https://stackoverflow.com/questions/3855127/find-and-kill-process-locking-port-3000-on-mac)



**How to rename a git branch?**
```
git branch -m new-name        
```
  * [Rename a Local and Remote Branch](https://multiplestates.wordpress.com/2015/02/05/rename-a-local-and-remote-branch-in-git/)



**How to find my current environment path?**
```
pip -V
pip 19.0.3 from /Users/yzabc/anaconda3/envs/py36/lib/python3.6/site-packages/pip (python 3.6)   
```
  * [Determine if you Python is running inside Virtualenv](https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv)




```
pip install pdftotext
    
you may need to install 
brew install poppler on Mac
```
  * [Unable to install pdftotext on Python 3.6](https://stackoverflow.com/questions/45912641/unable-to-install-pdftotext-on-python-3-6-missing-poppler)



**How to revert a single file to its previous commit?**
```
TBW 
```
  * [Reverting a single file to a previous version](https://stackoverflow.com/questions/2733873/reverting-a-single-file-to-a-previous-version-in-git/2734035)



**How to upload a custom emoji on Slack?**
```
TBW
```
* [How to add custom emoji to Slack](https://tryshift.com/blog/apps-hub/how-to-add-custom-emoji-to-slack/)




**How to open Jupyter lab?**
```
jupyter lab

http://localhost:8888/lab
```
* [How to start Jupyer](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)




**How to mirror github repo / how to git-mirror?**
``` 
git clone --bare https://github.com/kactLabs/kactKMNETL.git
cd kactKMNETL.git
git push --mirror https://github.com/rajasgs/kactKMNETLDec2019.git
cd ..
rm -rf kactKMNETL.git    
```
* [How to Mirror Sample repo](https://github.com/kactLabs/kactKMNETL)
* [Duplicating a Repo](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)



**How to fix "Failed to fetch"?**
```
    find the list in /etc/apt/sources.list.d
    and then remove it
    then apt-get update
```



**SSH key github**
```
TBW
```
* [Authenticating to GitHub](https://help.github.com/en/enterprise/2.17/user/authenticating-to-github/)
* [Adding a new ssh key to your Github account](https://help.github.com/en/enterprise/2.17/user/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
* [Ubuntu 18 - Setup ssh pulic key](https://www.cyberciti.biz/faq/ubuntu-18-04-setup-ssh-public-key-authentication/)



virtualenv
```
mkdir /envs
virtualenv --python=/usr/bin/python3.6 /envs/py36
cd /envs
source py36/bin/activate   
python --version
```
* [Use different python version with virtualenv](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)



**How to upload folder for beanstalk?**
```
cd /Users/yzabc/projects/eb-python-flask
zip ../eb-python-flask -r * .[^.]*
```





**Image2Table / im2table / i2t / im2t / img2table / image 2 table**
```
    https://snipboard.io/K9TYXf.jpg

    more:
    image2table.txt
```





**How to open jupyter notebook?**
```
jupyter notebook
or
jupyter lab
    
conda create -y python=3.6 --name py36az_jupyter
conda activate py36az_jupyter
conda deactivate

/Users/yzabc/projects/jupyterville
```
* [Jupyter Notebook - Beginner Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)
* [Jupyterwork samples](https://github.com/rajasgs/jupyterville)
* [Jupyter Notebook - Getting Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.htm)






**How to switch between two tabs in Ubunut/Mac?**
```
Command + Left arrow/Right arrow
```
https://unix.stackexchange.com/questions/67861/switch-between-tabs-in-gnome-terminal-with-keyboard










**How to uninstall docker in ubuntu?**
```

```
https://askubuntu.com/questions/935569/how-to-completely-uninstall-docker




**How to add a company in Crunchbase?**
https://www.crunchbase.com/add-new





**Rename files in a folder?**
```
pythonsamples/files_work/rename_files.py
```





**How to change ps1?**
```

```
https://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html





**How to install Hugo?**
```

```
https://www.thelinuxfaq.com/ubuntu/ubuntu-17-04-zesty-zapus/hugo?type=uninstall





**How to delete Garageband from mac?**
```
	Macintosh HD/Applications/GarageBand.app (1.16GB)
	Macintosh HD/Library/Application Support/GarageBand (995MB)
	Macintosh HD/Library/Application Support/Logic (880MB)
	Macintosh HD/Library/Audio/Apple Loops (up to 10GB)*
```
https://www.techjunkie.com/delete-garageband/




**How to enable/disable beautify in vscod?**

https://stackoverflow.com/questions/38057725/turn-off-auto-formatting-for-json-files-in-visual-studio-code





**How to install jupyterlab?**
```
TBW
```
https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html




**How to run gush file for another repo?**
```
/Users/rajacsp/d/gitmagic/gu.sh
just this command above
```





**How to change bash as your default shell?**
```

```
https://support.apple.com/en-ca/HT208050





**How to run jupyter?**
```
jupyter notebook
```





**How to install virtualvenv?**
```
https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d
```





**How to run luigi?**
```
  luigid
	http://localhost:8082/
```





**How to convert ppk to pem?**
```
	brew install putty
	puttygen key.ppk -O private-openssh -o key.pem
	http://www.codeblocq.com/2016/05/Convert-a-putty-ppk-key-to-a-pem-file-on-OSX/	
```





**ssh options**
```
ssh -i
https://www.ssh.com/ssh/command
```





**scp**
```

```
https://askubuntu.com/questions/312697/copy-files-from-remote-ubuntu-to-local-mac



