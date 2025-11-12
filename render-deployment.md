\ [Home](index.md)

# 🚀 How to Deploy on Render

Render makes it simple to host and scale web apps directly from your GitHub or GitLab repositories.  
Follow these steps to deploy your application in minutes.

---

## 🧩 Prerequisites

Before starting, make sure you have:

- A [Render](https://render.com) account  
- Your project pushed to **GitHub** or **GitLab**  
- A working app (Flask, Node.js, React, etc.)  
- A valid dependency file (`requirements.txt`, `package.json`, etc.)

---

## ⚙️ Step 1: Connect Your Repository

1. Log in to your [Render Dashboard](https://dashboard.render.com/).  
2. Click **New +** → **Web Service**.  
3. Connect your **GitHub** or **GitLab** account.  
4. Select the repository containing your project.  
5. Choose the branch you want to deploy (usually `main` or `master`).

---

## 🧾 Step 2: Configure Deployment Settings

1. Enter a **name** for your service (e.g., `my-web-app`).  
2. Select a **region** close to your users (e.g., Oregon or Frankfurt).  
3. Choose the **environment type**:
   - **Web Service** → For APIs, Flask, Django, Node.js, etc.  
   - **Static Site** → For HTML/CSS/JS or React apps  
4. Confirm the branch and click **Next**.

---

## 🧰 Step 3: Add Build and Start Commands

Set up commands based on your tech stack:

### 🐍 Python (Flask/Django)
- **Build Command:**  
  ```bash
  pip install -r requirements.txt

## 🔐 Step 4: Add Environment Variables

If your application uses environment variables (for example, database URLs, API keys, or secret tokens):

1. Go to your service → Environment tab.
2. Click Add Environment Variable.
3. Enter the key-value pairs, for example:

    ```bash
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://user:password@host:port/dbname

## 🚀 Step 5: Deploy Your App

**After setup:**
1. Click Create Web Service.

**Render will:**

1. Clone your repository
2. Install dependencies
3. Build and start your app

**Once deployed, your live URL will look like:**

1. https://your-app-name.onrender.com