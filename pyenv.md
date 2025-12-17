/ [Home](index.md)

## Pyenv



## 1. Prerequisites

Ensure **Homebrew** is installed:

```bash
brew --version
```

If not installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 2. Install pyenv via Homebrew

```bash
brew update
brew install pyenv
```

Verify installation:

```bash
pyenv --version
```

---

## 3. Configure Shell Environment

You must initialize `pyenv` in your shell startup file.

### For **zsh** (default on modern macOS)

Edit `~/.zshrc`:

```bash
nano ~/.zshrc
```

Add **at the end**:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Apply changes:

```bash
source ~/.zshrc
```

### For **bash**

Edit `~/.bashrc` or `~/.bash_profile`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

---

## 4. Install Python Build Dependencies (Important)

macOS requires additional libraries to compile Python properly:

```bash
brew install openssl readline sqlite3 xz zlib tcl-tk
```

For Apple Silicon, also run:

```bash
export LDFLAGS="-L$(brew --prefix openssl)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include"
```

(You may add these exports to your shell config if needed.)

---

## 5. Install a Python Version

List available versions:

```bash
pyenv install --list
```

Install a specific version (example):

```bash
pyenv install 3.11.9
```

Set it globally:

```bash
pyenv global 3.11.9
```

Or per project:

```bash
cd your-project
pyenv local 3.11.9
```

Verify:

```bash
python --version
which python
```

---

## 6. Optional: pyenv-virtualenv (Highly Recommended)

```bash
brew install pyenv-virtualenv
```

Add to `~/.zshrc`:

```bash
eval "$(pyenv virtualenv-init -)"
```

Create a virtualenv:

```bash
pyenv virtualenv 3.11.9 myenv
pyenv activate myenv
```

---

## 7. Common Troubleshooting

### pyenv not found after install

```bash
brew --prefix pyenv
echo $PATH
```

Ensure `~/.pyenv/bin` is **before system Python** in PATH.

### Python build fails

```bash
xcode-select --install
```

### Conflicts with Conda

If you use Conda, **do not auto-activate base**:

```bash
conda config --set auto_activate_base false
```

Restart terminal.

---

## Summary (Quick Install)

```bash
brew install pyenv
brew install openssl readline sqlite3 xz zlib tcl-tk

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

source ~/.zshrc
pyenv install 3.11.9
pyenv global 3.11.9
```

---
