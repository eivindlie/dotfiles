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

function aws-profile-env(){
    eval "$(aws configure export-credentials --profile $1 --format env)"
}

function r() {
    # Interactive repo picker.
    cd "$(find "${REPOS[@]}" -type d -maxdepth 1 | fzf)" || exit
}

function cc() {
    # Interactive repo picker, opens VSCode.
    code "$(find ${REPOS[@]} -type d -maxdepth 1 | fzf)" || exit
}

function code() {
    if [[ -d $1 ]]; then
        if ls $1/*.code-workspace 1> /dev/null 2>&1; then
            echo "A workspace file was found in the directory."
            read -q "REPLY?Are you sure you want to open the directory? [y/n] "
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                return
            fi
        fi
    fi
    command code $1
}

function lmk-isbn() {
    if [[ -z $1 ]]; then
        echo "Usage: lmk-isbn <isbn>"
        return 1
    fi

    local should_open=false
    if [[ $1 == "--open" ]]; then
        should_open=true
        shift  # Remove the --open flag from the arguments
    fi

    for isbn in "$@"; do
        # Ignore if argument starts with a dash
        if [[ $isbn == -* ]]; then
            continue
        fi
        
        if [[ $isbn =~ ^[0-9]{10}$ || $isbn =~ ^[0-9]{13}$ ]]; then
            local base64_isbn=$(echo -n "urn:isbn:$isbn" | base64)
            local url="https://laeremiddelkatalogen.sikt.no/moduler/$base64_isbn"
            echo "$url"
            if $should_open; then
                open "$url" &>/dev/null
            fi
        else
            echo "Invalid ISBN: $isbn"
        fi
    done
}