/ [Home](index.md)

## Ngrok (Windows Setup)

### 1. Create Ngrok Account

1. Go to the Ngrok website: [https://ngrok.com/](https://ngrok.com/)
2. Sign up or log in (Gmail login is faster and simpler).
3. After login, open the **Dashboard**.

---

### 2. Download Ngrok for Windows

1. Navigate to the official download page from the dashboard.
2. Download **Windows (64-bit)** version.
3. You will receive a ZIP file (e.g., `ngrok-v3-stable-windows-amd64.zip`).

---

### 3. Extract Ngrok

1. Right-click the ZIP file → **Extract All**.
2. Move `ngrok.exe` to a permanent location, for example:

   ```
   C:\ngrok\ngrok.exe
   ```

Avoid keeping it inside the Downloads folder.

---

### 4. Authenticate Ngrok (One-Time Setup)

Ngrok requires authentication to work reliably.

1. Open **Command Prompt**.
2. Navigate to the ngrok folder:

   ```bat
   cd C:\ngrok
   ```
3. Add your auth token (available in Ngrok Dashboard):

   ```bat
   ngrok config add-authtoken <yourtoken>
   ```

If this step is skipped, tunnels may fail or disconnect unexpectedly.

---

### 5. Verify Installation

Check if ngrok is installed correctly:

```bat
ngrok version
```

If the command is not recognized, the PATH is not set correctly.

---

### 6. Commands

#### Forward Local Server

Expose a local application running on port 80:

```bat
ngrok http 80
```

Example output will include a public URL like:

```
https://xxxx-xx.ngrok-free.app
```

---

#### Using Static (Permanent) Domain

If you have configured a static domain in the Ngrok dashboard:

```bat
ngrok http --domain=<your-static-domain> 80
```

Static domains are available only on paid plans.

---

### Notes

* Ngrok free URLs change every session.
* Ngrok is meant for **development and testing**, not production hosting.
* Always ensure your local server is running before starting ngrok.
