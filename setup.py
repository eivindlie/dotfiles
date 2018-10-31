import os
home = os.path.expanduser("~")


def setup_git():
    name = input('Enter full name (for gitconfig): ')
    email = input('Enter email (for gitconfig): ')

    with open('git/.gitconfig', 'r') as f:
        gitconfig = f.read()

    gitconfig = gitconfig.format(name, email)

    try:
        os.rename(os.path.join(home, '.gitconfig'), os.path.join(home, '.gitconfig.bak'))
    except WindowsError:
        pass

    with open(os.path.join(home, '.gitconfig'), 'w') as f:
        f.write(gitconfig)

    os.link('git/.gitconfig-symlink', os.path.join(home, '.gitconfig-symlink'))


def main():
    setup_git()


if __name__ == '__main__':
    main()
