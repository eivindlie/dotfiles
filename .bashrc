alias ll='ls -al --color=auto'
alias untar='tar -zxvf '
alias ping='ping -c 5'
alias cls='clear'
alias c='clear'
alias ls='ls --color=auto'
alias mkdir='mkdir -pv'
alias ports='netstat -tulanp'
alias rm='rm -I --preserve-root'
alias wget='wget -c'
alias ..='cd ..'

function git-prune-local {
  git fetch -p && for branch in $(git for-each-ref --format '%(refname) %(upstream:track)' refs/heads | awk '$2 == "[gone]" {sub("refs/heads/", "", $1); print $1}'); do git branch -D $branch; done
}