/ [Home](index.md)

# Conda Commands

### Install Miniconda in Ubuntu
```
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

conda config --set auto_activate_base false
```


### Install Miniconda in windows
```
Go to https://docs.conda.io/en/latest/miniconda.html
Select Python 3.8
```
[ref](https://docs.conda.io/en/latest/miniconda.html)


### How to verify Miniconda in Windows?
```
Type miniconda in your "Windows app search box" and you will get something like this

(TBA)
```

### Conda Basic Commands
```
conda --version
conda info
conda info --envs
conda env list

conda create -n test12 python=3.12

conda activate py311

pip list

conda list

conda list | grep "numpy"

conda deactivate

# dangerous
conda remove -n py311 --all
```


### How to create a conda environment by using miniconda
```
Open Anaconda/Miniconda Prompt and run as admin
You should see like this:

(base) 

Run this command:
conda create -n py12 -y python=3.12

To activate conda:
conda activate py12

To deactivate:
conda deactivate
```


### Create Conda environment
```
conda create -n pyone
conda activate pyone
conda deactivate pyone
```

### How to verify Python and version?
```
In your console (conda prompt), type this:
python --version

You should see
python 3.8
```

### Create an environment with specific python version
```
conda create -y python=3.6 --name py36
conda activate py36
conda deactivate
```

### Conda Py27
```
conda create -n py27 -y python=2.7
conda activate py27
conda deactivate
```


### How to view all environments
```
conda info --envs

or

conda env list

or

pip -V

```



### Sources :

  * [Conda]([file](https://salishsea-meopar-docs.readthedocs.io/en/latest/work_env/python3_conda_environment.html))
  * [](https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv)
  * [](https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory)
