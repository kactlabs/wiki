/ [Home](index.md)

## Git Fork and Bring Original Changes

## How to Update Your Fork with the Original Repo’s Latest Changes

## 1. Add the original repository as **upstream**

Run this once inside your local clone:

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git
```

Verify:

```bash
git remote -v
```

Expected:

* `origin` → your fork
* `upstream` → original repo

---

## 2. Fetch latest updates from the upstream repo

```bash
git fetch upstream
```

---

## 3. Merge (or rebase) upstream changes into your local `main`

```bash
git checkout main
git merge upstream/main
```

Alternative (linear history):

```bash
git rebase upstream/main
```

---

## 4. Push updated `main` branch to your fork

```bash
git push origin main
```

---

## **Short Version**

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---