/ [Home](index.md)
# n8n Installation Guide

This guide provides steps to install n8n using Docker Desktop on various operating systems.

## Common Requirement for All OS

You must install Docker Desktop first.

Download: https://www.docker.com/products/docker-desktop/

After installing, make sure:

* Docker is running
* You accepted WSL2 install (Windows)
* You see Docker icon running in taskbar/menu

## Windows – Installation Steps

1. Install Docker Desktop
   * Download Docker Desktop for Windows
   * Enable Hyper-V or WSL2 when asked
   * Restart your system

2. Open Command Prompt or PowerShell

3. Run n8n Docker container:
```bash
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

4. Open browser:
   * http://localhost:5678

🥳 n8n is running!

## Linux – Installation Steps

(Works on Ubuntu, Debian, CentOS)

1. Update packages
```bash
sudo apt update && sudo apt upgrade -y
```

2. Install Docker
   * Ubuntu:
```bash
sudo apt install docker.io -y
```

3. Enable & start Docker
```bash
sudo systemctl enable --now docker
```

4. Add your user to docker group
```bash
sudo usermod -aG docker $USER
```
(Reboot or log out & in)

5. Run n8n
```bash
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

6. Open browser
   * http://<your_server_ip>:5678

💥 Done!

## macOS – Installation Steps

1. Install Docker Desktop (Mac)
   * For Intel chip → Intel DMG
   * For M1/M2 → Apple Silicon DMG

2. Launch Docker
   * Make sure Docker is running.

3. Open Terminal
   * (can use Spotlight search)

4. Run n8n
```bash
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

5. Open browser:
   * http://localhost:5678

🎉 You're in!

## 🔁 To Stop n8n

Press:
```
CTRL + C
```

🚫 Important Note
Using:
```
--rm
```
means container is deleted on stop,
but workflows stay safe in volume ✅

## Recommended Background Mode

If you don't want the terminal open:
```bash
docker run -d --restart=always --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Then stop anytime:
```bash
docker stop n8n
```

And start again:
```bash
docker start n8n
```

## Optional Authentication (Recommended)
```bash
-e N8N_BASIC_AUTH_ACTIVE=true \
-e N8N_BASIC_AUTH_USER=admin \
-e N8N_BASIC_AUTH_PASSWORD=StrongPass123 \
