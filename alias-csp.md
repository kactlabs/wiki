/ [Home](index.md)

## Alias CSP / alias-csp

### Updated Date: 20260423
```
# Define a variable for the common path
USER_BASE_PATH="$HOME/rj"
KACT_BASE_PATH="$HOME/kact"
MYSHELL_PATH="$KACT_BASE_PATH/myshell"

alias py="python"

# Trash backup
# alias rm="trash"
unset rm

# Zshco and soume
alias zshco="code ~/.zshrc"
alias zeco="zshco"
alias zco="zeco"
alias zshko="kiro ~/.zshrc"
alias zeko="zshko"
alias zko="zeko"
alias rmf="rm -rf"
alias soume="source ~/.zshrc"
alias sourcez="soume"
alias sme="soume"

# absolete
alias txts="cd /Users/tactlabs/d/txts"
alias txti="cd /Users/tactlabs/d/txts"
alias txt="cd /Users/tactlabs/d/txts"
alias tactxi="cd /Users/tactlabs/d/tact_space/tact_txts"
alias bsc="cd $KACT_BASE_PATH/brave-search-custom"

# ip
alias wip="curl https://ifconfig.me/ -w '\n'"
alias ip="curl https://ifconfig.me/ -w '\n'"

alias bashing="code ~/.zshrc"
alias bashin="code ~/.zshrc"
alias zsin="code ~/.zshrc"
alias bashcat="cat ~/.bash_profile"

# pipi
alias pip='python -m pip'
alias pipi="python -m pip install -r requirements.txt"
alias piper="pipi"
alias pi="pipi"
alias pid="python -m pip install -r requirements-dev.txt"
alias pipim="python -m pip install -r requirements_macos.txt"
alias pim="pipim"
alias pshow="pip show"
alias pavail="pip index versions"
alias pil="pavail"

alias sshb="ssh-add -K ~/.ssh/id_rsa" # ssh base (for emergency purpose only)
alias tip="python $KACT_BASE_PATH/tactpip/tinstaller.py -p "
alias tup="python $KACT_BASE_PATH/tactpip/tinstaller.py -u "
alias tshow="python $KACT_BASE_PATH/tactpip/tshow.py "
alias cate="conda activate"
alias nb="jupyter notebook"
alias jlab="jupyter lab"
alias jlad="jlab --debug"
alias eli="clear"
alias app="py app.py"
alias ap="app"
alias play="py cricket.py"
alias cls="clear"
alias cde="conda deactivate"
alias ls2="ls -hal"
alias ho38="conda activate ho38"
alias ktl="kubectl"
alias ktx="kubectx"
alias kai="cd $HOME/d/kaipulla_space"
alias golyrics="$KACT_BASE_PATH/lyrics-analyzer-browser-extenson"
alias goly="golyrics"
alias gol="goly"
alias awsl="aws --endpoint-url=http://localhost:4566"
alias codez="code ~/.zshrc"
alias kexec="ktl exec -it"
alias dexec="docker exec -it"
alias goprod="ssh -i $HOME/.tact/creds/tact1_key.pem ubuntu@54.186.8.196"
alias co="code"
alias ko="kiro"
alias k="ko ."
alias cd..="cd .."
alias wp="which python"

# kactii
alias goka="ssh -i $HOME/.creds/kactii/kactii-2025.pem azureuser@57.151.97.192"
alias gok="goka"
alias gk1="gok"
alias goka2="ssh -i $HOME/.creds/kactii/kactii-2025.pem azureuser@20.55.89.108"
alias gok2="goka2"
alias gk2="goka2"
alias s="subl"

# docker
alias dcup="docker-compose up"
alias dup="dcup"
alias dcub="docker-compose up --build"
alias dps="docker ps"
alias dipsy='docker ps --format "table {{.Names}}\t{{.Status}}" | while read line; do 
    if [[ "$line" =~ "Up" ]]; then
        echo -e "\033[32m$line\033[0m"  # Green for running containers
    elif [[ "$line" =~ "Exited" ]]; then
        echo -e "\033[31m$line\033[0m"  # Red for stopped containers
    else
        echo -e "$line"
    fi
done'
alias dpy="dipsy"

alias genbranch="$MYSHELL_PATH/generate_branches_md.sh"
alias genb="genbranch"



# conda
alias ml312="conda activate ml312"
alias ml12="ml312"
alias m12="ml12"
alias genai11="conda activate genai11"
alias gai11="genai11"
alias g11="gai11"
alias py39="conda activate py39"
alias py37="conda activate py37"
alias c39="conda activate py39"
alias ml39="conda activate ml39"
alias py38="conda activate py38"
alias py311="conda activate py311"
alias py12="conda activate py312"
alias py11="conda activate py311"
alias p11="conda activate py311"
alias ml38="conda activate ml38"
alias cact="conda activate"
alias clist="conda env list"
alias cvl="clist"
alias test12="conda activate test12"
alias t12="test12"
alias m12="conda activate mcp12"

# git alias - borrowed from tact
# git 
alias gow="git show"
alias gl="git log"
alias gl2="gl -2"
alias gl2="gl -2"
alias gmirror="$MYSHELL_PATH/gmirror.sh"
alias gmr="gmirror"
alias gsus="git status"
alias gacm="gad && gcm"
alias gbra="git branch -a"
alias gull="git pull"
alias gul="gull"
alias gad="git add ."
alias gcm="git commit -m"
alias gish="git push"
alias gush="$MYSHELL_PATH/gitmagic/gu.sh"
alias gh="gush"
alias ghi="$MYSHELL_PATH/gitmagic/gu.sh"  # AI-powered git commit
alias gci="$MYSHELL_PATH/git_commit_ai.sh"
alias gimmit="git commit -m "
alias gull="git pull"
alias gcm="gimmit"
alias gp="git pull"
alias gck="git checkout"
alias gcl="git clone"
alias gus="git status"
alias gid="git diff"
alias gpl="git pull"
alias gdiff="git diff"
alias gdf="gdiff"
alias gip="git pull"
alias rmg="rm -rf .git"
alias git-https-url="git remote get-url --push origin | sed 's/git@github.com:/https:\/\/github.com\//' | sed 's/\.git$//'"
alias gurl="git-https-url"
alias grl="gurl"
alias gl2="git log -2"
alias grh="git reset --hard"
alias gcf="git clean -fd"
alias gsh="git stash"
alias gsa="gsh apply"
alias gmc2="git status --porcelain | grep '^ M' | wc -l" # git modified lines count
alias m2p="mod2pip"
alias m2pv="m2p --validate-env"

alias rj="cd $USER_BASE_PATH"
# alias gitmagic=""

# secret key maker
alias secret_key="openssl rand -hex 32"
alias sk="secret_key"

# csp personal
alias csp="cd $USER_BASE_PATH"
alias plogs="cd $USER_BASE_PATH/dailylogs"
alias plog="plogs"
alias plg="plog"
alias kc="cd $KACT_BASE_PATH/kactii-courses"
alias lma="cd $KACT_BASE_PATH/llm-adapter"

# mysh
alias cignore="$MYSHELL_PATH/cignore.sh"
alias cig="cignore"
alias ckiro="$MYSHELL_PATH/ckiro.sh"
alias ciro="ckiro"
alias cenv="cp $MYSHELL_PATH/.env.sample .env"
alias cant="$MYSHELL_PATH/cant.sh"
alias czem="$MYSHELL_PATH/czem.sh"
alias ctem="$MYSHELL_PATH/ctem.sh"
alias cfa="$MYSHELL_PATH/copy_fastapi_template.sh"
alias cfa2="$MYSHELL_PATH/copy_fastapi_template.sh 2"
alias cfa3="$MYSHELL_PATH/copy_fastapi_template.sh 3"
alias cfa4="$MYSHELL_PATH/copy_fastapi_template.sh 4"
alias cfa5="$MYSHELL_PATH/copy_fastapi_template.sh 5"
alias cfa6="$MYSHELL_PATH/copy_fastapi_template.sh 6"
alias cfa7="$MYSHELL_PATH/copy_fastapi_template.sh 7"
alias cfa8="$MYSHELL_PATH/copy_fastapi_template.sh 8"
alias myshel="cd $MYSHELL_PATH"
alias mysh="cd $MYSHELL_PATH"
alias libfinder="$MYSHELL_PATH/libenv.sh"
alias lf="libfinder"
alias rdf="$MYSHELL_PATH/rdf.sh"
alias lsfull="$MYSHELL_PATH/lsfull.sh"
alias gitbase="$MYSHELL_PATH/gitbase.sh"
alias pshow2="$MYSHELL_PATH/pshow2.sh"
alias pshow3="$MYSHELL_PATH/pshow3.sh"
alias pshow4="$MYSHELL_PATH/pshow4.sh"
alias ps2="pshow2"
alias ps3="pshow3"
alias ps4="pshow4"
alias gilly="gitbase kactlabs"
alias gly="gilly"
alias gcsp="gitbase rajacsp"
alias gac="gitbase kactii-academy"
alias mir="mkdir"
alias branches="$MYSHELL_PATH/branch_finder.sh"
alias bes="branches"
alias smon="$MYSHELL_PATH/submodule_or_not.sh"
alias op="open ."
alias zshb="$MYSHELL_PATH/zsh_backup.sh"
alias zb="zshb"
alias mir2="$MYSHELL_PATH/mir2.sh"
alias gtog="$MYSHELL_PATH/gtog.sh"


# mysh-precommit
alias prec="$MYSHELL_PATH/kactii_custom_precommit_hook.sh"

# 
alias tct="$HOME/kact"
alias tt="tct"
alias pyv="python --version"
alias cpe="cp .env.sample .env"

# 
alias cu="cursor"
alias shown="ncdu --color dark --exclude='.DS_Store'"
alias show="shown"

# fastapi
alias uvan="uvicorn app:app"
# alias uv="uvan"
# alias uvr="uv --reload"
unset uv

# copy kiro basics
alias ckb="cp -r $KACT_BASE_PATH/kiro-basics/.kiro ."

# copy vode basics
alias cvb="cp -r $KACT_BASE_PATH/vode-basics/.vode ."

# venv & uv
alias sov="source .venv/bin/activate"
alias ded="deactivate"
alias dea="ded"
alias upipi="uv pip install -r requirements.txt"
alias upi="upipi"

# ollama
alias ol="ollama"
alias oll="ol list"
alias opl="ollama pull"
alias ols="ol serve"
alias ogrep="ol list | grep "
alias olg="ogrep"
alias oll2="ollama list | awk 'NR>1 {print \$1}'"

# creds
alias gocreds="ko $HOME/.creds"
alias goc="gocreds"

# misc
alias pe.="pip install -e ."
alias pyl="pylint"

# ls++
alias ls3="ls -d */ | tr -d '/' | tr '\n' ' ' ; echo"

# Folder
alias tpy="cd $HOME/kact/tact-python"
alias tp="tpy"
alias dset="$HOME/datasets"
alias gaily="cd $HOME/kact/genai-daily"
alias pcl="cd $KACT_BASE_PATH/tact-html-public-clone"

# 
alias grepa="alias | grep"
alias gpa="grepa"
alias greph="history | grep"

# vercel
alias vpr="vercel --prod"

# tact-python
alias sta="py generate_stats.py"

# odin 
# alias od="cd ~/odin"
# alias odp="cd ~/odin/odin-playground"
# alias dow="~/Downloads"
# alias wenv='[ -f .env ] && source .env && echo "${SERVER_ENV:-staging}" | tr "[:upper:]" "[:lower:]"'
# alias goprod="cp .env.prod .env"
# alias gop="goprod"
# alias gostage="cp .env.staging .env"
# alias gost="gostage"
# alias gos="gost"
unset gostage
unset gost

# 
alias kact="cd $KACT_BASE_PATH"
alias kt="kact"
alias wiki="cd $KACT_BASE_PATH/wiki"
alias wi="wiki"
alias html="cd $KACT_BASE_PATH/tact-html"
alias rce="cd $KACT_BASE_PATH/random-certificates"
alias rpf="cd $KACT_BASE_PATH/random-pdf"
alias rr="cd $KACT_BASE_PATH/random-resume-collection"

# kact
alias ta="cd $KACT_BASE_PATH/"
alias tct="ta"

# jupyter
alias jl="jupyter lab"

# ls commands
alias l1="ls -1"

# misc
alias pkill="kill -9 "
alias pk="pkill"
alias lport="lsof -i "
alias lp="lport"
alias ngh="ngrok http"
alias gomemos="cd ~/Library/Group\ Containers/group.com.apple.VoiceMemos.shared/Recordings"
alias gome=gomemos
alias grepl="ls | grep "

# Mac Info
alias macinfo="system_profiler SPHardwareDataType SPDisplaysDataType SPMemoryDataType"
alias minfo="macinfo"

# creds
alias showcreds="cat ~/.creds/creds.txt"
alias scr="showcreds"

# Tree Commands
alias t2="tree -L 2"
alias t3="tree -L 3"
alias t5="tree -L 5"

## Llama:
alias lcp="llama-server -hf ggml-org/gemma-3-1b-it-GGUF --port 8080"

##
alias cv="cd $KACT_BASE_PATH/code-vectra"
# alias 

# rust
alias rc="rustc"
alias cb="cargo build"
alias crun="cargo run"
alias cbi="cargo build --release && cargo install --path ."
alias cr="crun"

# posh - kact themes
alias kposh="~/kact-poshthemes/configure.sh"
alias kps="kposh"
alias ez="exec zsh"

# picoclaw
alias pc="picoclaw"
alias pca="picoclaw agent"

# code-vectra
alias cvc="cd $HOME/kact/code-vectra"

# podcast maker
alias pod="py podcastmaker.py"
alias pd="pod"

# claude
alias cla="claude"

# make server
alias mds="make devserver"
alias mp="make publish"

# gab
alias gab="cd $KACT_BASE_PATH/rajacsp.github.io"

# Git opts
git-opts() {
  git "$1" --help | grep -E '^\s+(-[a-zA-Z]|--[a-zA-Z])' | grep -oE '(-[a-zA-Z]|--[a-zA-Z][a-zA-Z-]*)' | sort -u
}
```

