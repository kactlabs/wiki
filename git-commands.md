/ [Home](index.md)

# Git Commands

**Note:** Git commands



### Basic flow: (basis status check, add, commit, push)
```
git status
git add .
git commit -m "dc-00: comment"
git push
git diff *_client.html
git checkout -- abc.java
git commit filename
git diff --cached [filename]
git diff HEAD [filename]
```




### Git Basic and Medium Commands
```
# Git Commands Reference

---

## 🔵 Basic Commands

---

### Check current branch

```bash
git branch
```

Lists all local branches. The **active branch** is highlighted (usually green with an asterisk `*`).

---

### Switch to another branch

```bash
git checkout branch-name

# Example
git checkout agentscope-react-integration
```

Moves your working directory to the specified branch. All files update to reflect that branch's state.

---

### Pull latest changes from remote

```bash
git pull
```

Fetches changes from the remote (e.g. GitHub) and merges them into your current branch. Equivalent to `git fetch` + `git merge`.

---

### View recent commit history

```bash
git log -2          # Last 2 commits
git log -5          # Last 5 commits
git log --oneline   # Compact one-line view
```

Shows commit hash, author, date, and message. `--oneline` is great for a quick overview.

---

### Discard changes to a specific file

```bash
git checkout sample.py
```

Reverts `sample.py` back to the last committed version. Any unsaved edits to that file are **permanently lost**.

---

### Discard changes to all modified files

```bash
git checkout .
```

Reverts **all modified tracked files** in the current directory back to their last committed state. Does **not** remove new (untracked) files.

---

### Delete all new (untracked) files

```bash
git clean -fd
```

Removes all **untracked files and directories**. Use with caution — this cannot be undone.

| Flag | Meaning |
|------|---------|
| `-f` | Force (required by default) |
| `-d` | Also remove untracked directories |

Dry-run first with `git clean -nfd` to preview what will be deleted.

---

## 🟡 Medium Commands

---

### Create and switch to a new branch

```bash
git checkout -b new-branch-name

# Example
git checkout -b feature/agent-memory
```

Creates a new branch from your current position and immediately switches to it. Shorthand for `git branch` + `git checkout`.

---

### Stage files for commit

```bash
git add sample.py        # Stage a specific file
git add .                # Stage all changes in current directory
git add src/             # Stage all changes in a folder
```

Moves changes into the **staging area** (index), ready to be committed.

---

### Commit staged changes

```bash
git commit -m "Your commit message here"
```

Saves a snapshot of all staged changes to the local repository. Good messages follow: `type: short description` (e.g. `feat: add memory agent`).

---

### Push a branch to remote

```bash
git push origin branch-name

# Example
git push origin feature/agent-memory
```

Uploads your local branch to the remote repository. First push of a new branch may require `-u` to set upstream:

```bash
git push -u origin feature/agent-memory
```

---

### View status of working directory

```bash
git status
```

Shows which files are modified, staged, or untracked. Run this constantly — it's your ground truth.

---

### View what actually changed (diff)

```bash
git diff                  # Unstaged changes
git diff --staged         # Staged changes (ready to commit)
git diff branch-a branch-b  # Compare two branches
```

Shows line-by-line what was added (`+`) or removed (`-`).

---

### Stash work-in-progress

```bash
git stash           # Save current changes temporarily
git stash pop       # Restore the most recent stash
git stash list      # View all stashes
git stash drop      # Delete the most recent stash
```

Stashing lets you set aside dirty work without committing, so you can switch branches cleanly and come back later.

---

### Merge another branch into current branch

```bash
git merge branch-name

# Example (from main, pull in a feature branch)
git merge feature/agent-memory
```

Combines the history of `branch-name` into your current branch. If there are conflicts, Git will flag them for manual resolution.

---

### Rebase current branch onto another

```bash
git rebase main
```

Replays your branch's commits on top of `main`, giving a **linear history** instead of a merge commit. Preferred in many teams for cleaner logs. Avoid rebasing shared/public branches.

---

### Undo the last commit (keep changes)

```bash
git reset --soft HEAD~1
```

Moves `HEAD` back one commit but **keeps your changes staged**. Useful if you committed too early.

```bash
git reset --mixed HEAD~1   # Unstages changes but keeps files
git reset --hard HEAD~1    # ⚠️ Discards changes entirely
```

---

### View remote URLs

```bash
git remote -v
```

Shows the fetch and push URLs for your configured remotes (usually `origin`).

---

### Fetch without merging

```bash
git fetch origin
```

Downloads changes from remote but does **not** merge them. Lets you inspect before integrating. Use `git log origin/main` after to review.

---

### Tag a commit (e.g. a release)

```bash
git tag v1.0.0
git tag v1.0.0 abc1234    # Tag a specific commit hash
git push origin v1.0.0    # Push tag to remote
```

Tags mark specific points in history — typically used for releases or milestones.

---

## 🔑 Quick Reference

| Command | What it does |
|--------|--------------|
| `git branch` | List branches |
| `git checkout branch` | Switch branch |
| `git checkout -b branch` | Create + switch |
| `git pull` | Fetch + merge from remote |
| `git status` | Show working directory state |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit staged changes |
| `git push origin branch` | Push to remote |
| `git diff` | Show unstaged diffs |
| `git log --oneline` | Compact history |
| `git stash` | Temporarily save changes |
| `git merge branch` | Merge a branch in |
| `git rebase main` | Replay commits on top of main |
| `git reset --soft HEAD~1` | Undo last commit, keep changes |
| `git checkout .` | Discard all modified tracked files |
| `git clean -fd` | Remove all untracked files/dirs |
```


### Configure user details on Git
```
git config --global user.email "abc@gmail.com"
git config --global user.name "Your Name"
```




### Git cache / github password cache:
```
git config credential.helper store
```




### Reset a single file:
```
git checkout filename
```
Ref:
[Revert a single file](http://www.norbauer.com/rails-consulting/notes/git-revert-reset-a-single-file.html)




### Git commit some files
[Commit only some files](http://stackoverflow.com/questions/7239333/how-do-i-commit-only-some-files)




### End git diff
```
type q
```




### Revert last push
```
git reset --hard <revision_id_of_last_known_good_commit>
git push --force
```
[Rollback last push](http://stackoverflow.com/questions/6655052/is-there-a-way-to-rollback-my-last-push-to-git)




### Add all except a single file
```
git add .
git reset filename
```




### Git logs:
```
git log
```




### Git logs with limit
```
git log -n 2
```




### Git previous logs one line
```
git log --pretty=oneline
```




### Git stats
```
git log --stat
git log --stat -n 2
```




### Git log for particular author
```
git log --author="rajacsp" -n 2
```




### ### Git log graph
```
git log --graph --decorate --oneline
```
Ref:
* [View commit history](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
* [Inspecting a repository](https://www.atlassian.com/git/tutorials/inspecting-a-repository)
* [Git status](https://git-scm.com/docs/git-status)




### Revert all uncommitted changes including new files
Revert changes to modified files
```
git reset --hard
```




### Remove all untracked files and directories. (`-f` is `force`, `-d` is `remove directories`)
```
git clean -fd
```




### Undo a last add before commit
```
git reset
```




### Revert a single file
```
git checkout filename
```
[Revert reset a single file](http://www.norbauer.com/rails-consulting/notes/git-revert-reset-a-single-file.html)




### Git add all but ignore one file
```
git add -u
git reset -- filename.txt
```




### Revert one uncommitted file git
```
git checkout abc.php
```
[Revert a single file](http://www.norbauer.com/rails-consulting/notes/git-revert-reset-a-single-file.html)




### Clone
```
git clone https://github.com/rajacsp/drivercheck
```




### Ignore class files git
```
/*.class in gitignore
```
[Ignore files in Git](http://stackoverflow.com/questions/4308610/how-to-ignore-certain-files-in-git)



### Short log
```
git shortlog -s
```
will get all users' commit by count




### Total commits count in Head, Branch and All
```
git rev-list --count HEAD
	- will get the total commits in head
git rev-list --all --count
	- will get the total commits in all
git rev-list --count origin/K-develop
```
[Get Git commit count](https://stackoverflow.com/questions/677436/how-do-i-get-the-git-commit-count)




### Caching your GitHub password in Git:
[Cache Password](https://help.github.com/articles/caching-your-github-password-in-git/)



### Take branch
```
git checkout -b branch_name
```
[Create a new branch](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches)




### Clone the right branch
```
git clone abc.git branch abc_branch
```




### Merge branch with Master (puhsing branch's code into master): verified on Feb 10, 2017
```
go inside master folder:
git checkout master
git pull origin master
git merge branch_name
git push origin master
```



### If conflict occurs, fix them using method below:
```
 <<<<<<< HEAD - old code start
 =======      - old code end
 >>>>>>> plainreport - new code end
```
	How to fix Git merge conflicts:
	[Fix Git Merge](https://www.youtube.com/watch?v=g8BRcB9NLp4)




### How to merge a new branch with master?
```
git checkout master
git pull origin master
git merge branch_name
git push origin master
```
[Merge](http://stackoverflow.com/questions/5601931/best-and-safest-way-to-merge-a-git-branch-into-master)




```
git pull origin K-develop
git merge origin/K-develop
git push
```

### Gitk
```
How to install gitk in MacOs?
brew update
brew install git
brew install git-gui

	ref:
	https://stackoverflow.com/questions/17582685/install-gitk-on-mac

How to install gitk on Ubuntu?
<TBD>
```

### Git Tags
```
git tag v1.0

git tag -a v1.1 -m "Second version"

git tag

git show v1.0

git tag -l "v1.*"

git push origin v1.0

git push origin --tags

git push --tags

git tag -d v1.0

git push origin -d v.10

git checkout tags/v1.0

git fetch --all
```
[Git and GitHub Beginner Tutorial 7 - Git Tags - what, why, when and how](https://www.youtube.com/watch?v=govmXpDGLpo)
[What is git tag, How to create tags & How to checkout git remote tag(s)](https://stackoverflow.com/questions/35979642/what-is-git-tag-how-to-create-tags-how-to-checkout-git-remote-tags)
[How To Delete Local and Remote Tags on Git](https://devconnected.com/how-to-delete-local-and-remote-tags-on-git/)


### How to delete a branch locally and remotely
```
// delete branch locally
git branch -d localBranchName

// delete branch remotely
git push origin --delete remoteBranchName
```
[How to delete a branch](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/)


### Find Git Version in cmd
```
git --version
git version 2.16.2.windows.1
```
if you get "command not found", it simply means that you haven't installed
[Git Version](http://superuser.com/questions/347728/terminal-command-to-find-what-version-of-git-i-have-installed)



### Pull Request:
[pull-request](https://help.github.com/articles/about-pull-requests/


### Git Cherry pick
```
git cherry-pick <commit-id>
```
* [Cherry pick](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-cherry-pick.html)
* [Merge](https://stackoverflow.com/questions/881092/how-to-merge-a-specific-commit-in-git)
* [Pull Alll commit](https://stackoverflow.com/questions/880957/pull-all-commits-from-a-branch-push-specified-commits-to-another/881014#881014)
* [pull reqeust](http://markosullivan.ca/how-to-handle-a-pull-request-from-github/)




### Rewrite old history in GIT
```
java -jar c:/bfg/bfg-1.13.0.jar --delete-file *.mp3 pythonsamples.git
java -jar c:/bfg/bfg-1.13.0.jar --strip-blobs-bigger-than 30M pythonsamples.git
cd pythonsamples.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```
[Bfg cleaner](https://rtyley.github.io/bfg-repo-cleaner/#usage)




### Rename previous commit
```
git commit --amend -m "TACT-436: Script alignment made"
```




### Change commit message after git push
```
git commit --amend -m "Message"
git push --force-with-lease
```
[Change git commit](https://stackoverflow.com/questions/8981194/changing-git-commit-message-after-push-given-that-no-one-pulled-from-remote)


OR


```
git rebase -i eb5661a8e4de761d2af79c5ecbdbc875c34481fa
```
[Edit commit message](https://superuser.com/questions/751699/is-there-a-way-to-edit-a-commit-message-in-github/751909)



### Stash existing changes
```
git stash     (will stash your existing changes)
git pull      (pull all of your new changes from central repository)
git stash apply (bring back your old changes on top of new code)
```
[Stashing](https://git-scm.com/book/en/v1/Git-Tools-Stashing)





### View stash files
```
git stash show
```
* [Preview Stash content](https://stackoverflow.com/questions/3573623/is-it-possible-to-preview-stash-contents-in-git)

* [Git credentials](https://stackoverflow.com/questions/11693074/git-credential-cache-is-not-a-git-command)


### List stash
```
git stash list
```


### Save/Apply Stash by Name
```
git stash save <stash_name>
git status apply stash^{/stash_name}

git stash save abc
git stash apply stash^{/abc}
```
[more](https://stackoverflow.com/questions/11269256/how-to-name-and-retrieve-a-stash-by-name-in-git)


### Delete a branch
```
git push -d <remote_name> <branch_name>
git branch -d <branch_name>

delete multiple branches:
git push -d <remote_name> <branch_name_1> <branch_name_2>
```
* [Delete Git branch](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely)
* [Delete multiple branch](https://stackoverflow.com/questions/3670355/can-you-delete-multiple-branches-in-one-command-with-git)



Git Tutorial:
[Git Fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch)

git cheat sheet:
[Git Cheat sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)

git commands:
[Git commands](https://www.siteground.com/tutorials/git/commands.htm)

[Setting up a repo](https://www.atlassian.com/git/tutorials/setting-up-a-repository)

more:
[Saving changes](https://www.atlassian.com/git/tutorials/saving-changes)


Copy Repository with history:
[Copying a full git repo](https://developer.atlassian.com/blog/2016/01/totw-copying-a-full-git-repo/)


```
git status -uno
```



### Get all commits
```
git rev-list --all --pretty=oneline
```
https://stackoverflow.com/questions/1314950/git-get-all-commits-and-blobs-they-created







### How to cherry pick
```
git checkout p (target branch)
git cherry-pick <commit_id>
```



Check diff
https://stackoverflow.com/questions/436362/how-to-diff-a-commit-with-its-parent/449128#449128




### How to find the parent branch?
```
git parent
```
https://stackoverflow.com/questions/3161204/find-the-parent-branch-of-a-git-branch







### When did I create a branch?
```
git reflog --date=local
git reflog --date=local feat-feature-endpoint-p
```
https://stackoverflow.com/questions/2255416/how-to-determine-when-a-git-branch-was-created







### Create a branch from another branch
```
git checkout -b myfeature dev
```
https://stackoverflow.com/questions/4470523/create-a-branch-in-git-from-another-branch






### How to rename a branch name?
https://stackoverflow.com/questions/6591213/how-do-i-rename-a-local-git-branch






### Git diff and apply
```
git diff new-feature..new-feature2 | git apply -
```







### Find the parent branch: (buggy as well)
```
git for-each-ref --format='%(refname:short)' refs/heads/* | while read b; do if r=$(git config --get branch.$b.remote); then m=$(git config --get branch.$b.merge); echo "$b -> $r/${m##*/}"; fi; done
```
https://blog.liplex.de/git-show-parent-branch/






### Git Rebase
https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase








```
git bi-sect
```
https://git-scm.com/docs/git-bisect



Git rebase manual vs Git rebase interactive
Ref needed


Git rebase vs git merge
https://stackoverflow.com/questions/804115/when-do-you-use-git-rebase-instead-of-git-merge



When should I git pull rebase
https://stackoverflow.com/questions/2472254/when-should-i-use-git-pull-rebase








### Merge vs pull
```
git pull origin master
is same as
git fetch origin
git merge origin/master
```
https://stackoverflow.com/questions/21756614/difference-between-git-merge-origin-master-and-git-pull







### Merge another branch changes into mine
```
https://help.github.com/en/articles/merging-an-upstream-repository-into-your-fork
```







### Show which files have been changed from another branch
```
git diff --name-status another_branch
git diff --name-status feat-product-apply-permission-K20-1382-latest
git diff --name-status p
```
https://stackoverflow.com/questions/822811/showing-which-files-have-changed-between-two-revisions






### Delete a branch
```
git branch -D branch_name
```
https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely







### Git stash
```
git stash list
```
will list all stashes

https://git-scm.com/docs/git-stash







### Show git username
```
git config user.name
git config --list
```
https://alvinalexander.com/git/git-show-change-username-email-address







### View file in another branch
https://stackoverflow.com/questions/7856416/view-a-file-in-a-different-git-branch-without-changing-branches



### Undo pushed commits
https://stackoverflow.com/questions/22682870/git-undo-pushed-commits



### How to revoke last pushed commit?
(ref needed)


### Get the old check point
```
git checkout 85d29a6c0853f85303f87091efd8b3ac9ca69766
```








```
git add .
git commit -m "Last commit revoked"fa
git push origin HEAD:master -f
```







### How to merge my branch to master in git?
```
git checkout master
git pull https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git BRANCH_NAME
git push origin master
```








```
git push --set-upstream origin qa
git push --set-upstream origin feat-raja-one
```






### Merge branch to qa
```
git pull
git checkout qa
git pull
git pull https://github.com/rajasgs/merge-test feat-raja-one
git push origin qa
```
[Merging an upstream repository into your fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/merging-an-upstream-repository-into-your-fork)







### How to mirror github repo?
```
git clone --bare https://github.com/kactLabs/kactKMNETL.git
cd kactKMNETL.git
git push --mirror https://github.com/rajasgs/kactKMNETLDec2019.git
cd ..
rm -rf kactKMNETL.git
```
[Duplicating a repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)






### How to change the committed message?
```
git amend
git commit --amend -m "Message"
```
[Rewriting History](https://www.atlassian.com/git/tutorials/rewriting-history)



### How to change the remote url?
```
git remote set-url origin git@github.com:username/reponame.git

ref:
https://chatgpt.com/share/6c4af7db-f6cd-4bcf-956a-1b550b4b882e
```



### How to check your current remote url?
```
git remote -v

you will something like this
origin	git@github.com:kactlabs/reponame.git (fetch)
origin	git@github.com:kactlabs/reponame.git (push)
```


### Credits
  * [submodules] (https://github.blog/2016-02-01-working-with-submodules/)


### Git Advanced
Below is the requested content **converted into clean, structured Markdown format**.

---


### How to migrate from master branch to main
```
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```