/ [Home](index.md)

# Error Log / Error Archive

**Note:** Error Matters a lot at Kact!



### Template
```
---------------------------------------------------------------------------------------------------------------/

Paste your Error Here

---------------------------------------------------------------------------------------------------------------/
```


### Sample
```

---------------------------------------------------------------------------------------------------------------/







127.0.0.1 - - [30/Mar/2021 19:45:58] "GET / HTTP/1.0" 200 -
[Errno 17] File exists: './static'
static/simple-flask.zip
Unzipped
Uploaded
[run_python_venv] app_folder :  simple-flask
created virtual environment CPython3.8.5.final.0-64 in 320ms
  creator CPython3Posix(dest=/home/ubuntu/kact/experimental-space/rjdeploy/simple-flask/.venv, clear=False, global=False)
  seeder FromAppData(download=False, appdirs=latest, CacheControl=latest, retrying=latest, colorama=latest, pep517=latest, progress=latest, lockfile=latest, setuptools=latest, pip=latest, packaging=latest, six=latest, certifi=latest, distro=latest, wheel=latest, pkg_resources=latest, ipaddr=latest, contextlib2=latest, distlib=latest, msgpack=latest, requests=latest, html5lib=latest, pytoml=latest, pyparsing=latest, idna=latest, webencodings=latest, chardet=latest, urllib3=latest, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv/seed-app-data/v1.0.1.debian)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
./deploy.sh: 4: source: not found
Requirement already satisfied: flask in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.1.2)
Requirement already satisfied: Werkzeug>=0.15 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (1.0.1)
Requirement already satisfied: itsdangerous>=0.24 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: Jinja2>=2.10.1 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (2.11.2)
Requirement already satisfied: click>=5.1 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (7.1.2)
Requirement already satisfied: MarkupSafe>=0.23 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask->-r requirements.txt (line 1)) (1.1.1)
Deployed with Pip
s2 3009
Traceback (most recent call last):
  File "/home/ubuntu/kact/experimental-space/kact-lambda/app.py", line 8, in <module>
    from flask import Flask, render_template, jsonify, request
ModuleNotFoundError: No module named 'flask'







---------------------------------------------------------------------------------------------------------------/




(py38) ubuntu@ip-172-31-29-189:~/kact/experimental-space/kact-lambda$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:3024/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 238-292-004
[Errno 17] File exists: './static'
127.0.0.1 - - [31/Mar/2021 06:21:57] "GET /data HTTP/1.0" 200 -



[Errno 17] File exists: './static'
static/simple-flask.zip
Unzipped
Uploaded
created virtual environment CPython3.8.5.final.0-64 in 339ms
  creator CPython3Posix(dest=/home/ubuntu/kact/experimental-space/rjdeploy/simple-flask/.venv, clear=False, global=False)
  seeder FromAppData(download=False, appdirs=latest, CacheControl=latest, retrying=latest, colorama=latest, pep517=latest, progress=latest, lockfile=latest, setuptools=latest, pip=latest, packaging=latest, six=latest, certifi=latest, distro=latest, wheel=latest, pkg_resources=latest, ipaddr=latest, contextlib2=latest, distlib=latest, msgpack=latest, requests=latest, html5lib=latest, pytoml=latest, pyparsing=latest, idna=latest, webencodings=latest, chardet=latest, urllib3=latest, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv/seed-app-data/v1.0.1.debian)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
./deploy.sh: 4: source: not found
The current working directory: /home/ubuntu/kact/experimental-space/rjdeploy/simple-flask
Python 3.8.8
Requirement already satisfied: flask in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.1.2)
Requirement already satisfied: click>=5.1 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (7.1.2)
Requirement already satisfied: Jinja2>=2.10.1 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (2.11.2)
Requirement already satisfied: itsdangerous>=0.24 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: Werkzeug>=0.15 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from flask->-r requirements.txt (line 1)) (1.0.1)
Requirement already satisfied: MarkupSafe>=0.23 in /home/ubuntu/miniconda3/envs/py38/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask->-r requirements.txt (line 1)) (1.1.1)
s4 3009
nohup: appending output to 'nohup.out'
Traceback (most recent call last):
  File "/home/ubuntu/kact/experimental-space/kact-lambda/app.py", line 8, in <module>
    from flask import Flask, render_template, jsonify, request
ModuleNotFoundError: No module named 'flask'







---------------------------------------------------------------------------------------------------------------/


```
