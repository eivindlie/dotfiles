import os
home = os.path.expanduser("~")

def setup_git():
    name = input('Enter full name (for gitconfig): ')
    email = input('Enter email (for gitconfig): ')

    with open('git/.gitconfig', 'r') as f:
        gitconfig = f.read()

    gitconfig = gitconfig.format(name, email)

    with open(os.path.join(home, '.gitconfig'), 'w') as f:
        f.write(gitconfig)

def main():
    setup_git()

if __name__ == '__main__':
    main()