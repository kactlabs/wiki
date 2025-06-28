/ [Home](index.md)

# How to set evironment variable in Ubuntu

**Note:** You need an environment variable, right?



Settting environment variable option 1
```
export TACT_ENV='local_kact_env'

verify:
printenv TACT_ENV

verify:
echo $TACT_ENV
```

Settting environment variable option 2
```
echo "export RJ_ENV='this_is_my_env_variable'" > rj.env

source ./rj.env

python
	> import os;os.environ.get('RJ_ENV')
```

Unset environment variable
```
export TACT_ENV=

unset TACT_ENV

export -n TACT_ENV
```

##### Ref :

  * [Askubuntu - How do I set environment variable](https://askubuntu.com/questions/730/how-do-i-set-environment-variables)
  * [Environment Variables](https://help.ubuntu.com/community/EnvironmentVariables)

