/ [Home](index.md)

/ [Home](index.md)

# n8n Workspace Overview

This section explains the n8n workspace UI and common terminologies to help you understand how to build workflows efficiently.

## 🏠 n8n Workspace Layout (After Login)

When you open n8n in the browser (`http://localhost:5678`), you will see the main workspace. It has multiple navigation elements:

---

### 🔹 Left Sidebar (Navigation Menu)

This contains all the global navigation options.

| Item                                   | Meaning / Usage                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Workflows**                          | List of all workflows created. You can create, edit, activate, or delete workflows from here.           |
| **Executions**                         | Shows workflow runs (successful or failed). Useful for debugging.                                       |
| **Credentials**                        | Stores API keys and authentication required to connect to apps (e.g., Google Sheets, Slack, Notion).    |
| **Users & Roles** *(Cloud/Enterprise)* | Manage multiple users, permissions, teams.                                                              |
| **Settings**                           | System-level settings: environment variables, logs, default timezone, execution settings, version info. |

---

### 🔹 Top Bar (Workflow Actions)

Seen when editing a workflow.

| Button / Feature             | What it does                                                             |
| ---------------------------- | ------------------------------------------------------------------------ |
| **Workflow Name**            | Rename the workflow for easy identification.                             |
| **Active / Inactive toggle** | Enables or disables the workflow. If active, triggers run automatically. |
| **Run Once**                 | Manually triggers/executes the workflow once.                            |
| **Save**                     | Saves the workflow changes.                                              |

---

### 🔹 Canvas / Editor Space

This is the visual editor where you build workflows.

* Drag nodes from the + menu onto the canvas.
* Connect nodes using arrows to build automation flow.
* You can zoom in/out and move around.

---

### 🔹 Node Panel (Right Side)

When you click on a node, the right panel opens.

| Section         | Details                                                  |
| --------------- | -------------------------------------------------------- |
| **Parameters**  | Where you provide inputs (API endpoint, payloads, etc.). |
| **Credentials** | Select saved auth credentials.                           |
| **Output**      | Shows node execution data (great for debugging).         |

---

## ⚙️ Key n8n Terminologies

| Term                  | Meaning                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------ |
| **Node**              | A single block representing an action or integration (API call, database query, logic operator, etc.). |
| **Trigger Node**      | Starts a workflow automatically (e.g., cron schedule, webhook call).                                   |
| **Regular Node**      | Executes after a trigger or another node (e.g., send email, update database).                          |
| **Workflow**          | A complete automation composed of nodes.                                                               |
| **Execution**         | A single run of a workflow. Can be manually run or auto-triggered.                                     |
| **Credentials**       | Stored authentication (OAuth/API key) used by nodes to connect to apps.                                |
| **Active Workflow**   | Runs automatically based on triggers.                                                                  |
| **Inactive Workflow** | Can only be manually executed.                                                                         |

---

## 🚀 Example Workflow Flow

```
[Trigger Node] → [Processing Nodes] → [Output Action Node]
   (Webhook)        (IF, Set, HTTP)       (Send Slack Message)
```

---

## 🔥 Pro Tips

✅ Always store API keys inside **Credentials**, not inside nodes directly.

✅ Use **Executions** to replay/debug failed runs.

✅ Use **IF**, **Switch**, **Merge**, **Wait**, and **Function Node** for logic-based workflows.

✅ Use built-in **Webhooks** to integrate with external apps.

---

You're ready to start building workflows! 🎉
