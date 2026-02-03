# How to Install WSL in Windows

Here's the clean, correct way to install WSL (Windows Subsystem for Linux) on Windows. This guide covers the modern one-command method first (recommended), then the manual fallback.

## ✅ Recommended Method (Windows 10 21H2+ / Windows 11)

### 1️⃣ Open PowerShell as Administrator

- Press **Start**
- Type **PowerShell**
- Right-click → **Run as administrator**

### 2️⃣ Run this single command

```bash
wsl --install
```

**What this does automatically:**
- Enables WSL
- Enables Virtual Machine Platform
- Installs WSL 2
- Installs Ubuntu (default distro)
- Sets WSL 2 as default

👉 **Reboot when prompted**

### 3️⃣ Launch Linux

After reboot:
- Open **Start**
- Search **Ubuntu**
- First launch will ask you to:
  - Create a Linux username
  - Create a password

🎉 **Done.** You now have a full Linux environment.

### 🔍 Verify Installation

```bash
wsl --status
```

You should see:
- Default version: 2
- Installed distribution: Ubuntu

---

## 📋 Common WSL Commands

### Install a specific distribution

```bash
wsl --install -d <DistroName>
```

### List available distributions

```bash
wsl --list --online
```

### Set default distribution

```bash
wsl --set-default <DistroName>
```

### Set default version

```bash
wsl --set-default-version 2
```

### Uninstall a distribution

```bash
wsl --unregister <DistroName>
```

### Update WSL

```bash
wsl --update
```

### Shutdown WSL

```bash
wsl --shutdown
```

---

## 🔄 File Access

### Access Windows files from WSL

```bash
cd /mnt/c/Users/<username>
```

### Access WSL files from Windows

```bash
\\wsl$\<DistroName>
```

---

## 🛠️ Advanced Commands

### Run a command in WSL

```bash
wsl <command>
```

### Run a command in a specific distribution

```bash
wsl -d <DistroName> <command>
```

### Run a command as a specific user

```bash
wsl -u <username> <command>
```

### Export a distribution

```bash
wsl --export <DistroName> <FileName>
```

### Import a distribution

```bash
wsl --import <DistroName> <InstallLocation> <FileName>
```

### Terminate a distribution

```bash
wsl --terminate <DistroName>
```

### List running distributions

```bash
wsl --list --running
```

### List all distributions

```bash
wsl --list --all
```

### List verbose

```bash
wsl --list --verbose
```
