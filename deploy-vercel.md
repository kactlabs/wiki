/ [Home](index.md)

# Deploy a flask app with Vercel


### How to setup Vercel CLI (MacOS)
```
node -v
npm -v

brew install node

npm install -g vercel

# verify
vercel --version
```

### How to setup Vercel CLI (Ubuntu)
```

```

### How to setup Vercel CLI (Windows)
```

```


### How login on vercel?
```
vercel login
```

### Flask app

- create a folder named "api"
- create "requirements.txt" file and "vercel.json" file
- create "app.py" and templates folder
- templates => html files( for example, index.html)
- use the following template for vercel.json file:
    ```
    {
    "rewrites": [
      { 
          "source": "/(.*)", "destination": "/api/app.py" 
      }
    
        ] 
    }
    ```

### Git push

- Run your flask app in local system
- Git push your project

### Login to vercel

```
https://vercel.com
```
- Create an account in vercel and login to the page
- Continue with Github and allow github authentication.
- Select only specfic repositories and import 
- Set a Domain name and click Deploy
- The deploy logs will be displayed and any error while deployment will be shown.

### Congratulations! You have Deployed your flask app.



# Vercel Deployment Guide for KBot

Complete guide for deploying and debugging KBot on Vercel.

## Prerequisites

- Vercel account (sign up at https://vercel.com)
- Vercel CLI installed: `npm i -g vercel`
- Git repository with your KBot code

## Initial Deployment

### Option 1: Deploy via Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Import your Git repository (GitHub, GitLab, or Bitbucket)
4. Configure project:
   - **Framework Preset**: Other
   - **Build Command**: Leave empty (or `pip install -r requirements.txt`)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`
5. Add **Environment Variables**:
   - `SLACK_BOT_TOKEN` = `xoxb-your-bot-token`
   - `SLACK_SIGNING_SECRET` = `your-signing-secret`
6. Click **"Deploy"**

### Option 2: Deploy via CLI

```bash
# Login to Vercel
vercel login

# Deploy to production
vercel --prod

# Follow the prompts to link your project
```

## Environment Variables

### Add Environment Variables

**Via Dashboard:**
1. Go to https://vercel.com/dashboard
2. Select your `slack-kbot` project
3. Go to **Settings** → **Environment Variables**
4. Click **"Add New"**
5. Add each variable:
   - Key: `SLACK_BOT_TOKEN`
   - Value: `xoxb-your-actual-token`
   - Environment: Production, Preview, Development (select all)
6. Repeat for `SLACK_SIGNING_SECRET`

**Via CLI:**
```bash
# Add environment variable
vercel env add SLACK_BOT_TOKEN production
# Paste your token when prompted

vercel env add SLACK_SIGNING_SECRET production
# Paste your secret when prompted
```

### Update Environment Variables

If you need to update a token (e.g., after adding new Slack scopes):

**Via Dashboard:**
1. Go to **Settings** → **Environment Variables**
2. Find the variable (e.g., `SLACK_BOT_TOKEN`)
3. Click **"Edit"** (pencil icon)
4. Update the value
5. Click **"Save"**
6. **Important**: Redeploy your app for changes to take effect

**Via CLI:**
```bash
# Remove old variable
vercel env rm SLACK_BOT_TOKEN production

# Add new variable
vercel env add SLACK_BOT_TOKEN production
```

### After Updating Environment Variables

⚠️ **You must redeploy for changes to take effect!**

**Via Dashboard:**
1. Go to **Deployments** tab
2. Click the three dots (**...**) on the latest deployment
3. Click **"Redeploy"**
4. Confirm the redeployment

**Via CLI:**
```bash
vercel --prod
```

## Viewing Logs

### Via Dashboard (Recommended)

1. Go to https://vercel.com/dashboard
2. Click on your `slack-kbot` project
3. Click **Deployments** tab
4. Click on the latest deployment
5. Click **Functions** tab
6. View real-time logs with filters:
   - Filter by status (200, 404, 500, etc.)
   - Filter by time range
   - Search for specific text

### Via CLI

**View logs for a specific deployment:**
```bash
# Get deployment URL first
vercel ls

# View logs (replace with your actual URL)
vercel logs https://slack-kbot.vercel.app

# Or use deployment ID
vercel logs dpl_xxxxxxxxxxxxx
```

**View logs as JSON (for parsing with jq):**
```bash
vercel logs https://slack-kbot.vercel.app --json

# Filter for errors only
vercel logs https://slack-kbot.vercel.app --json | jq 'select(.statusCode >= 400)'

# Filter for Slack API errors
vercel logs https://slack-kbot.vercel.app --json | jq 'select(.message | contains("Slack API error"))'
```

**Common CLI commands:**
```bash
# List all deployments
vercel ls

# List deployments for specific project
vercel ls slack-kbot

# Get deployment details
vercel inspect https://slack-kbot.vercel.app

# View project info
vercel project ls
```

## Testing Your Deployment

### Test Endpoints

```bash
# Test root endpoint (should return unique ID)
curl https://slack-kbot.vercel.app/
# Expected: {"unique_id":"7262-20260128"}

# Test health endpoint
curl https://slack-kbot.vercel.app/health
# Expected: {"status":"healthy","bot":"KBot"}

# Test Slack events endpoint (will fail without proper signature)
curl -X POST https://slack-kbot.vercel.app/slack/events
# Expected: 401 Unauthorized (this is correct - signature required)
```

### Check Deployment Status

```bash
# Via CLI
vercel ls

# Via browser
# Go to: https://slack-kbot.vercel.app/health
```

## Common Issues and Debugging

### Issue 1: "Slack API error: missing_scope"

**Symptoms:**
- Bot receives messages but doesn't respond
- Logs show: `Slack API error: missing_scope`

**Cause:**
- The `SLACK_BOT_TOKEN` in Vercel is outdated
- You added new scopes in Slack but didn't update the token in Vercel

**Fix:**
1. Go to Slack API → OAuth & Permissions
2. Copy the current Bot User OAuth Token
3. Update `SLACK_BOT_TOKEN` in Vercel (Settings → Environment Variables)
4. Redeploy the app

### Issue 2: "invalid_auth" or "not_authed"

**Symptoms:**
- Logs show: `Slack API error: invalid_auth`

**Cause:**
- Wrong token in Vercel
- Using App-Level Token (`xoxe-`) instead of Bot Token (`xoxb-`)

**Fix:**
1. Verify you're using Bot User OAuth Token (starts with `xoxb-`)
2. Update `SLACK_BOT_TOKEN` in Vercel
3. Redeploy

### Issue 3: Bot doesn't receive events

**Symptoms:**
- No logs appear when you message the bot
- `/slack/events` endpoint not being called

**Cause:**
- Event Subscriptions URL not configured in Slack
- URL not verified (no green checkmark)

**Fix:**
1. Go to Slack API → Event Subscriptions
2. Set Request URL to: `https://slack-kbot.vercel.app/slack/events`
3. Wait for green checkmark ✅ "Verified"
4. Make sure bot events are added (`message.im`, etc.)
5. Reinstall app to workspace

### Issue 4: "Invalid signature" errors

**Symptoms:**
- Logs show: `Invalid request signature`
- 401 Unauthorized responses

**Cause:**
- Wrong `SLACK_SIGNING_SECRET` in Vercel
- Extra spaces in environment variable

**Fix:**
1. Go to Slack API → Basic Information → App Credentials
2. Copy Signing Secret (click "Show")
3. Update `SLACK_SIGNING_SECRET` in Vercel (no extra spaces!)
4. Redeploy

### Issue 5: Deployment fails

**Symptoms:**
- Build fails
- "Error: No Python version specified"

**Fix:**
Create `runtime.txt` in your project root:
```
python-3.11
```

Or create `vercel.json`:
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Issue 6: Can't find deployment with CLI

**Symptoms:**
- `vercel logs slack-kbot` fails
- Error: "Can't find the deployment"

**Fix:**
```bash
# Link to the project first
vercel link

# Or use the full URL
vercel logs https://slack-kbot.vercel.app

# Or list deployments first
vercel ls
```

## Monitoring

### Real-time Monitoring

**Via Dashboard:**
1. Go to your project → **Deployments**
2. Click latest deployment → **Functions**
3. Logs update in real-time
4. Use filters to find specific issues

**Via CLI:**
```bash
# Follow logs in real-time
vercel logs https://slack-kbot.vercel.app --follow
```

### Check for Errors

**In Dashboard:**
- Look for red status codes (400, 500, etc.)
- Filter by "Error" level
- Check "Messages" column for error details

**Via CLI:**
```bash
# Get logs as JSON and filter for errors
vercel logs https://slack-kbot.vercel.app --json | jq 'select(.statusCode >= 400)'
```

### Common Log Messages

| Message | Meaning | Action |
|---------|---------|--------|
| `URL verification challenge received` | Slack verifying your endpoint | ✅ Normal |
| `Message sent to channel` | Bot successfully replied | ✅ Normal |
| `Invalid request signature` | Wrong signing secret | Update `SLACK_SIGNING_SECRET` |
| `Slack API error: missing_scope` | Token missing permissions | Update `SLACK_BOT_TOKEN` |
| `Slack API error: invalid_auth` | Wrong or expired token | Update `SLACK_BOT_TOKEN` |
| `Duplicate event ignored` | Event deduplication working | ✅ Normal |

## Redeployment

### When to Redeploy

Redeploy after:
- Updating environment variables
- Changing code
- Adding new dependencies to `requirements.txt`
- Updating Slack scopes (after updating token in Vercel)

### How to Redeploy

**Via Dashboard:**
1. Go to **Deployments** tab
2. Click three dots on latest deployment
3. Click **"Redeploy"**
4. Confirm

**Via CLI:**
```bash
# Redeploy current code
vercel --prod

# Force redeploy without changes
vercel --prod --force
```

**Via Git:**
```bash
# Push to your main branch
git push origin main

# Vercel auto-deploys on push (if connected to Git)
```

## Rollback

If a deployment breaks something:

**Via Dashboard:**
1. Go to **Deployments** tab
2. Find a working deployment
3. Click three dots → **"Promote to Production"**

**Via CLI:**
```bash
# List deployments
vercel ls

# Promote a specific deployment
vercel promote <deployment-url>
```

## Custom Domain (Optional)

### Add Custom Domain

1. Go to **Settings** → **Domains**
2. Click **"Add"**
3. Enter your domain (e.g., `kbot.yourdomain.com`)
4. Follow DNS configuration instructions
5. Update Slack Event Subscriptions URL to your custom domain

## Performance Tips

1. **Use Production Environment**: Always deploy with `--prod` flag
2. **Monitor Cold Starts**: Serverless functions may have cold starts
3. **Keep Dependencies Minimal**: Only include required packages
4. **Use Logging**: Add strategic log points for debugging
5. **Set Timeouts**: Vercel has 10s timeout for Hobby plan, 60s for Pro

## Security Best Practices

1. **Never commit tokens**: Keep `.env` in `.gitignore`
2. **Use Environment Variables**: Store all secrets in Vercel
3. **Verify Signatures**: Always validate Slack signatures (already implemented)
4. **Rotate Tokens**: Periodically rotate your Slack tokens
5. **Monitor Logs**: Check for suspicious activity

## Useful Links

- [Vercel Dashboard](https://vercel.com/dashboard)
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel CLI Reference](https://vercel.com/docs/cli)
- [Vercel Python Runtime](https://vercel.com/docs/functions/runtimes/python)
- [Vercel Logs Documentation](https://vercel.com/docs/observability/runtime-logs)

## Support

If you encounter issues:
1. Check Vercel logs (Dashboard or CLI)
2. Verify environment variables are set correctly
3. Test endpoints with curl
4. Check Slack API dashboard for errors
5. Review Vercel status: https://www.vercel-status.com/

## Quick Reference

```bash
# Deploy
vercel --prod

# View logs
vercel logs https://slack-kbot.vercel.app

# List deployments
vercel ls

# Add environment variable
vercel env add VARIABLE_NAME production

# Remove environment variable
vercel env rm VARIABLE_NAME production

# Link project
vercel link

# Inspect deployment
vercel inspect https://slack-kbot.vercel.app

# Promote deployment to production
vercel promote <deployment-url>
```


### Vercel CLI 
```
vercel login

vercel link
Vercel CLI 48.2.9
? Set up “~/kact/slack-kbot”? yes
? Which scope should contain your project? TactEditor's projects
? Found project “tacteditors-projects/slack-kbot”. Link to it? yes
✅  Linked to tacteditors-projects/slack-kbot (created .vercel)


vercel ls

Vercel CLI 48.2.9
> Deployments for tacteditors-projects/slack-kbot [165ms]

  Age     Deployment                                                       Status      Environment     Duration     Username
  3m      https://slack-kbot-qpvvd0z1l-tacteditors-projects.vercel.app     ● Ready     Production      24s          tacteditor
  6m      https://slack-kbot-1cvohw9m6-tacteditors-projects.vercel.app     ● Ready     Production      13s          tacteditor

vercel logs <deployment-url>

vercel logs https://slack-kbot.vercel.app

vercel --prod

vercel env rm UNIQUE_COUNTRY production
printf "india" | vercel env add UNIQUE_COUNTRY production

vercel --prod

vercel --prod --force

vercel switch vipranan

vercel whoami
vercel teams ls

vercel logs

# Re-link to your personal account or correct team
vercel link
```