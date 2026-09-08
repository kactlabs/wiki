/ [Home](index.md)

## Ubuntu Setup

**Note:** 

1. Check Node.js and npm

```
node --version
npm --version
```

If Node.js isn't installed, the easiest option is:

```
sudo apt update
sudo apt install nodejs npm -y
```

```
node --version
npm --version
```

2. Install Node.js using NVM

```
Install NVM:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

Reload your shell:

source ~/.bashrc

Check:

nvm --version

Install Node.js LTS:

nvm install --lts

Use it:

nvm use --lts

Verify:

node --version
npm --version
```

3. Create your Electron project

```
mkdir electron-app
cd electron-app

Initialize npm:

npm init -y
```

4. Install Electron

```
npm install --save-dev electron

Check Electron:

npx electron --version
```

5. Run Electron

```
npm start
```

If Electron gives a sandbox error

```
The SUID sandbox helper binary was found, but is not configured correctly
```

Run

```
npx electron --no-sandbox .
```