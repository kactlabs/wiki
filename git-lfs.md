/ [Home](index.md)

## Git LFS

**Note:** git for large file systems

### Install LFS - Ubuntu
```
sudo apt update
sudo apt install git-lfs

git lfs version
```

### Install LFS - MacOS
```
brew install git-lfs

git lfs version
```

```
# tldr; 

git lfs install

git lfs track "*.pdf"

git add .gitattributes

git commit -m "Move large PDFs to Git LFS"
git push origin main
```


```bash
git lfs install

# Track the large PDF files
git lfs track "*.pdf"

# Add the .gitattributes file
git add .gitattributes

# Remove files from regular git and re-add with LFS
# Simpler approach - renormalize to apply LFS rules
git add --renormalize *.pdf

# Commit and push
git commit -m "Move large PDFs to Git LFS"
git push origin main
```


```bash

git config --global --list | grep lfs
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true

```


```
git lfs env

git-lfs/3.7.1 (GitHub; darwin arm64; go 1.25.3)
git version 2.39.5 (Apple Git-154)

Endpoint=https://github.com/kactlabs/minibooks.git/info/lfs (auth=none)
  SSH=git@github.com:kactlabs/minibooks.git
LocalWorkingDir=/Users/csp/kact/minibooks
LocalGitDir=/Users/csp/kact/minibooks/.git
LocalGitStorageDir=/Users/csp/kact/minibooks/.git
LocalMediaDir=/Users/csp/kact/minibooks/.git/lfs/objects
LocalReferenceDirs=
TempDir=/Users/csp/kact/minibooks/.git/lfs/tmp
ConcurrentTransfers=8
TusTransfers=false
BasicTransfersOnly=false
SkipDownloadErrors=false
FetchRecentAlways=false
FetchRecentRefsDays=7
FetchRecentCommitsDays=0
FetchRecentRefsIncludeRemotes=true
PruneOffsetDays=3
PruneVerifyRemoteAlways=false
PruneVerifyUnreachableAlways=false
PruneRemoteName=origin
LfsStorageDir=/Users/csp/kact/minibooks/.git/lfs
AccessDownload=none
AccessUpload=none
DownloadTransfers=basic,lfs-standalone-file,ssh
UploadTransfers=basic,lfs-standalone-file,ssh
GIT_EXEC_PATH=/Applications/Xcode.app/Contents/Developer/usr/libexec/git-core
git config filter.lfs.process = "git-lfs filter-process"
git config filter.lfs.smudge = "git-lfs smudge -- %f"
git config filter.lfs.clean = "git-lfs clean -- %f"
```


```
git lfs ls-files

d277fc6db5 * 1766540434140-langchain-snippets-20251224.pdf
b5eefa9ddc * 81-ai-agents-use-cases-20251116-1763313557925.pdf
a62d55e4c7 * GenAI Agents Marketplace for super-lazy.pdf
f791e815d3 * agent-quality-20251115.pdf
ba250ad8f5 * agentic-ai-an-executive-playbook-20251116-1763265171723.pdf
e98ee6f2e4 * agentic-ai–the-new-frontier-in-genai-20251026-1760535844138.pdf
b88fd3534e * ai-agents-65-use-cases-transforming-enterprises-20251114-1763091041771.pdf
5fd98ba272 * ai-engineer-roadmap-20251117.pdf
d44b7cff38 * artificial-intelligence-with-python-20251026-1760966923259.pdf
e9198e01f9 * build-a-voice-ai-agent-that-actually-sounds-human-step-by-step-tutorial-20251026-1761245957795.pdf
044add4505 * building-ai-voice-agents-20251115.pdf
0850af264a * chunking-techniques-1760239205095.pdf
c19044acc9 * context-engineering-sessions-memory-20251115.pdf
3d437da64b * genai-roadmap-1760050986776.pdf
3d437da64b * genai-roadmap-20251012-1760050986776.pdf
4bd0366ddf * introduction-to-agents-2025125.pdf
1091d429ee * kwikee-2-vision-final.pdf
3aa18d167e * llm-cheat-sheet-20251004-1759457996101.pdf
42772c3873 * mastering-llm-as-a-judge-20251026-1761450709978.pdf
ce6500bd59 * prototype-to-production-20251115.pdf
bed7179a1f * python-Cheatsheet-for-machine-learning-20251026-1761583696414.pdf
48d904bde6 * python-basics-sample-chapters.pdf
5b00bcb6ee * rag-playbook-1762748140720.pdf
9f3c9e395f * various-prompting-1759317813767.pdf
9f3c9e395f * various-prompting-20251012-1759317813767.pdf
```

---

### Ref:
[https://git-lfs.com/](https://git-lfs.com/)

---


## Chunk and Merge log files along with lfs
```

csp_mac_syslog-20251208_part_aa

git lfs track "csp_mac_syslog*"

cat csp_mac_syslog* > csp_mac_syslog.log

```

# Special Git Features Similar to Git LFS

Git offers several specialized mechanisms—native and external—that solve challenges around large files, repository scale, dependency management, workflow automation, and data governance.

---

## 1. Git LFS (Large File Storage)

**Purpose:** Efficient handling of large binary files
**Mechanism:** Replaces large files with pointers and stores actual content externally

**Use cases:**

* Media assets
* ML models
* Large datasets
* Compiled binaries

---

## 2. Git Submodules

**Purpose:** Embed one Git repository inside another

**Characteristics:**

* Separate version history
* Explicit commit locking
* Requires manual sync

```bash
git submodule add <repo-url>
git submodule update --init --recursive
```

**Ideal for:** Shared libraries, third-party dependencies

---

## 3. Git Subtree

**Purpose:** Alternative to submodules with tighter integration

**Characteristics:**

* Merges external repo into main tree
* No separate clone required
* Simplified deployment

**Best for:** When external code must behave like internal code

---

## 4. Git Sparse Checkout

**Purpose:** Checkout only specific directories

```bash
git sparse-checkout init
git sparse-checkout set path/to/folder
```

**Use cases:**

* Large monorepos
* Targeted development or CI jobs

---

## 5. Git Partial Clone

**Purpose:** Download objects only when required

```bash
git clone --filter=blob:none <repo>
```

**Use case:** Massive repositories with deep history

---

## 6. Git Hooks

**Purpose:** Automate actions based on Git events

**Common hooks:**

* `pre-commit`
* `commit-msg`
* `pre-push`
* `post-merge`

**Use cases:**

* Enforcing lint rules
* Security validation
* Build automation

---

## 7. Git Worktrees

**Purpose:** Multiple working directories from a single repository

```bash
git worktree add ../feature-xyz feature-xyz
```

**Use cases:**

* Parallel branch development
* Hotfix + feature isolation

---

## 8. Git Attributes (.gitattributes)

**Purpose:** Define behavior per file type

**Capabilities:**

* Custom diff rules
* LFS association
* Line ending normalization

```bash
*.zip filter=lfs diff=lfs merge=lfs -text
```

---

## 9. Git Clean / Smudge Filters

**Purpose:** Transform file content during commit or checkout
**Note:** Git LFS internally uses these filters

---

## 10. Git Notes

**Purpose:** Attach metadata to commits without changing history

**Use cases:**

* Audit annotations
* Reviewer comments
* Compliance notes

---

## 11. Git Annex (External Tool)

**Purpose:** Advanced large dataset management

**Capabilities:**

* Distributed storage
* Offline support
* Cloud syncing

**Best for:** Research and scientific data repositories

---

## 12. Git Crypt

**Purpose:** Encrypt specific repository files

**Use cases:**

* Secret configuration files
* Secure credentials

---

# Feature Comparison Matrix

| Feature         | Primary Function          | Git Native | External Tool |
| --------------- | ------------------------- | ---------- | ------------- |
| Git LFS         | Large file handling       | No         | Yes           |
| Submodules      | Repository dependencies   | Yes        | No            |
| Subtree         | Integrated external code  | Yes        | No            |
| Sparse Checkout | Partial repository access | Yes        | No            |
| Partial Clone   | Minimize clone size       | Yes        | No            |
| Hooks           | Workflow enforcement      | Yes        | No            |
| Worktrees       | Multi-branch workflows    | Yes        | No            |
| Git Annex       | TB-scale dataset control  | No         | Yes           |
| Git Crypt       | File encryption           | No         | Yes           |

---

# Strategic Selection Guide

### Use Git LFS when:

* Files exceed 50–100 MB
* Frequent binary versioning occurs

### Use Sparse Checkout / Partial Clone when:

* Repository is large but mostly text-based

### Use Git Annex when:

* Managing multi-terabyte datasets

### Use Git Worktrees when:

* Concurrent branch development is necessary

---

