alias ll='ls -al --color=auto'
alias untar='tar -zxvf '
alias ping='ping -c 5'
alias cls='clear'
alias c='clear'
alias ls='ls --color=auto'
alias mkdir='mkdir -pv'
alias ports='netstat -tulanp'
#alias rm='rm -I --preserve-root'
alias wget='wget -c'
alias ..='cd ..'
alias dc='docker compose'
alias django='pipenv run python manage.py'
alias kpdjango='dc exec app python manage.py'
alias kpkube='kubectl -n feide-feide-kp'
alias ntkkube='kubectl -n feide-nasjonal-tjenestekatalog'

function r() {
    # Interactive repo picker.
    cd "$(find "${REPOS[@]}" -type d -maxdepth 1 | fzf)" || exit
}

function cc() {
    # Interactive repo picker, opens VSCode.
    code "$(find ${REPOS[@]} -type d -maxdepth 1 | fzf)" || exit
}
