/ [Home](index.md)

### Postfix Setup Ubuntu

**Note:** You need email, right? then, follow these fudging guidelines!


#### Setup Postfix

1. Install postfix and libasl module
	sudo apt-get install libsasl2-modules postfix
	
2. Select 'Internet Site' General type of mail configuration
	
3. In system mail name, type your domain name
	kactti.com
	
4. Once the installation is complete, confirm myhostname param in /etc/postfix/main.cf
```
myhostname = kactii.com
```


#### Setup Gmail password to Posfix

**Veriy myhostname**
```
cat /etc/postfix/main.cf | grep "kactii"
myhostname = kactii.com
```

**Open sasl_password and update your Gmail app password**
```
vi /etc/postfix/sasl/sasl_passwd
[smtp.gmail.com]:587 xyz@kactii.com:enssmudsibcssagu
```

**Create a hash db file for Postfix**
```
sudo postmap /etc/postfix/sasl/sasl_passwd
```

**Verify the newly created file**
```
ls -hal /etc/postfix/sasl/sasl_passwd.db
```

**Change permissions for sasl_password**
```
sudo chown root:root /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
sudo chmod 0600 /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
```

**Configure postfix relay server**
```
vi /etc/postfix/main.cf

Update these:
relayhost = [smtp.gmail.com]:587

Add these at the end:

smtp_sasl_auth_enable = yes

smtp_sasl_security_options = noanonymous

smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd

smtp_tls_security_level = encrypt

smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```

**Restart postfix**
```
sudo systemctl restart postfix
```

**Verify by sending Email**
```
sendmail obama@gmail.com
From: xyz@talentaccurate.com
Subject: Fund us Obama
We are doing awesome things, so fund us!
.
```



##### Ref :

  * [Postfix setup with Gmail App Password](https://www.linode.com/docs/email/postfix/configure-postfix-to-send-mail-using-gmail-and-google-apps-on-debian-or-ubuntu/)
