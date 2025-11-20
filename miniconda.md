/ [Home](index.md)

# Miniconda 

**Note:** notes


Install Miniconda in Ubuntu
```
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

conda config --set auto_activate_base false
```



Install Miniconda in windows
```
Go to https://docs.conda.io/en/latest/miniconda.html
Select Python 3.8
```
[ref](https://docs.conda.io/en/latest/miniconda.html)


How to verify Miniconda in Windows?
```
Type miniconda in your "Windows app search box" and you will get something like this

(TBA)
```


How to create a conda environment by using miniconda
```
Open Miniconda Prompt and run as admin
You should see like this:

(base) 

Run this command:
conda create -n py12 -y python=3.12

To activate conda:
conda activate py12

To deactivate:
conda deactivate
```


How to verify Python and version?
```
In your console (conda prompt), type this:
python --version

You should see
python 3.8
```


### Ref :

  * [Name](file)
