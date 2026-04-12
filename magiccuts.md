/ [Home](index.md)

## Magiccuts

Shortcuts (magiccuts) we use to speed up our project work.

### Prerequisites

Clone the myshell repo first:

```bash
cd ~/kact
git clone git@github.com:kactlabs/myshell.git
```

### Setup

Open your `~/.zshrc` in an editor:

```bash
code ~/.zshrc
```

Then add all the following aliases to it:

```bash
KACT_BASE_PATH="$HOME/kact"
MYSHELL_PATH="$KACT_BASE_PATH/myshell"
```

### gilly

Git base shortcut for kactlabs.

```bash
alias gitbase="$MYSHELL_PATH/gitbase.sh"
alias gilly="gitbase kactlabs"
alias gly="gilly"
```

### cant

```bash
alias cant="$MYSHELL_PATH/cant.sh"
```

### cig

Shortcut for cignore.

```bash
alias cignore="$MYSHELL_PATH/cignore.sh"
alias cig="cignore"
```

### cfa8

FastAPI template copy shortcuts (cfa through cfa8).

```bash
alias cfa="$MYSHELL_PATH/copy_fastapi_template.sh"
alias cfa2="$MYSHELL_PATH/copy_fastapi_template.sh 2"
alias cfa3="$MYSHELL_PATH/copy_fastapi_template.sh 3"
alias cfa4="$MYSHELL_PATH/copy_fastapi_template.sh 4"
alias cfa5="$MYSHELL_PATH/copy_fastapi_template.sh 5"
alias cfa6="$MYSHELL_PATH/copy_fastapi_template.sh 6"
alias cfa7="$MYSHELL_PATH/copy_fastapi_template.sh 7"
alias cfa8="$MYSHELL_PATH/copy_fastapi_template.sh 8"
```
