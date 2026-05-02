/ [Home](index.md)

# Kact OS and Git Rules

**Note:** We apply these rules every day!



At Kact & KactLabs,

- We are NOT supposed to see **Windows** while screen sharing or at work
- We are NOT supposed to listen the word **Windows**
- We are NOT supposed to see **https** in GitHub. We always use git ssh not https
- Always work on a branch for you. Never commit on main branch without any permission.
- Always **git pull** before you start working
- Never leave having unpushed files. Before you leave, always **git commit** and **git push**
- Don't dump big images, files without your Manager approval
- We may have **main**, **dev**, **prod** branches
  - **main** - basic branch which is default
  - **dev** - developer based experimental branch
  - **prod** - production based branch
- Don't dump big objects into Git

```
du -sh .git/*
4.0K	.git/COMMIT_EDITMSG
4.0K	.git/FETCH_HEAD
4.0K	.git/HEAD
4.0K	.git/ORIG_HEAD
4.0K	.git/config
4.0K	.git/description
60K	.git/hooks
12K	.git/index
4.0K	.git/info
16K	.git/logs
387M	.git/objects
12K	.git/refs
```

If you see above, **387M** which is huge for a GitHub repo. We must fix these kind of issues before it is too late. If you don't know how to solve it, talk to your immediate Manager.


