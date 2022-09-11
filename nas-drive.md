/ [Home](index.md)

# NAS Drive




```
Most of our private data storedin NAS-Drive (Toronto)

Get the creds from TLs
```


How to share NAS data?
```

Share this format when you mention to Tactiians or update them GitHub:
/Tact/datasets-private/us-postal-codes/AK-zipcodes.json
http://gofile.me/6UZP3/HhqAB4MdM

```


How to share the data with custom password and share with public?
```
1. Right click the file and share
2. Enable Secure sharing
    Privacy Settings: Public - password protection
    Password: (custom password)
```


How to connect to NAS Drive via SSH?
```
1. Enable SSH in Control Panel -> Terminal & SNMP 
2. ssh username@NASNAME
    It should ask for password

    2.1. output: 
        username@abc's password:

        Synology strongly advises you not to run commands as the root user, who has
        the highest privileges on the system. Doing so may cause major damages
        to the system. Please note that if you choose to proceed, all consequences are
        at your own risk.

        Could not chdir to home directory /var/services/homes/username: No such file or directory

Ref:
https://www.timmertech.io/get-terminal-access-to-your-synology/
```



