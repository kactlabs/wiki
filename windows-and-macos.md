/ [Home](index.md)

## Windows and macOS Setup
 

**Note: Only for macOS users**

Install Homebrew (if not already installed)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

1. Check Node.js

```
node --version
npm --version
```

2. Create a project folder

```
mkdir electron-app
cd electron-app
```

3. Initialize the Node.js project

```
npm init -y
```

4. Install Electron

```
npm install --save-dev electron

npx electron --version
```

5. Run your Electron application

```
npm start
```