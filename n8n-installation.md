/ [Home](index.md)

# n8n Installation

Install n8n using Docker.

## Prerequisites

Install Docker Desktop: https://www.docker.com/products/docker-desktop/

Verify Docker is running before proceeding.

## Quick Start

Run n8n:
```bash
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access: http://localhost:5678

Stop: `CTRL + C`

## OS-Specific Setup

**Windows**
- Enable WSL2 or Hyper-V during Docker installation
- Restart after install

**Linux (Ubuntu/Debian)**
```bash
sudo apt update && sudo apt install docker.io -y
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```
Log out and back in, then run n8n command above.

**macOS**
- Download correct version (Intel or Apple Silicon)
- Ensure Docker is running before starting n8n

## Background Mode

Run n8n as a service:
```bash
docker run -d --restart=always --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Manage:
```bash
docker stop n8n
docker start n8n
```

## Authentication (Optional)

Add to docker run command:
```bash
-e N8N_BASIC_AUTH_ACTIVE=true \
-e N8N_BASIC_AUTH_USER=admin \
-e N8N_BASIC_AUTH_PASSWORD=YourPassword
```
