#!/usr/bin/env python3

from __future__ import print_function, with_statement
from builtins import input

import os
import platform

home = os.path.expanduser("~")
system = platform.system()

yes_answers = ('yes', 'YES', 'y', 'Y')


def setup_git():
    if input('Set up gitconfig? (yes/no) ') not in yes_answers:
        return
    name = input('Enter full name (for gitconfig): ')
    email = input('Enter email (for gitconfig): ')

    with open('git/.gitconfig', 'r') as f:
        gitconfig = f.read()

    gitconfig = gitconfig.format(name, email)

    if system == 'Windows':
        try:
            os.rename(os.path.join(home, '.gitconfig'),
                      os.path.join(home, '.gitconfig.bak'))
        except WindowsError:
            pass
    else:
        try:
            os.rename(os.path.join(home, '.gitconfig'),
                      os.path.join(home, '.gitconfig.bak'))
        except OSError:
            pass

    with open(os.path.join(home, '.gitconfig'), 'w') as f:
        f.write(gitconfig)

    os.symlink(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'git/.gitconfig-symlink'),
        os.path.join(home, '.gitconfig-symlink'))


def setup_bashrc():
    if input('Set up .bashrc? (yes/no) ') not in yes_answers:
        return

    if system == 'Windows':
        print('You are running Windows - .bashrc cannot be setup')
        return
    try:
        with open(os.path.join(home, '.bashrc')) as f:
            bashrc_content = f.read()
    except FileNotFoundError:
        bashrc_content = ''

    bashrc_content = 'source ~/.bashrc-symlink\n' + bashrc_content

    with open(os.path.join(home, '.bashrc'), 'w') as f:
        f.write(bashrc_content)

    try:
        os.rename(os.path.join(home, '.bashrc-symlink'),
                  os.path.join(home, '.bashrc-symlink.bak'))
    except OSError:
        pass

    os.symlink(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '.bashrc'),
        os.path.join(home, '.bashrc-symlink'))


def setup_zshrc():
    if input('Set up .zshrc? (yes/no) ') not in yes_answers:
        return

    if system == 'Windows':
        print('You are running Windows - .zshrc cannot be setup')
        return
    try:
        with open(os.path.join(home, '.zshrc')) as f:
            zshrc_content = f.read()
    except FileNotFoundError:
        zshrc_content = ''

    zshrc_content = 'source ~/.zshrc-symlink\n' + zshrc_content

    with open(os.path.join(home, '.zshrc'), 'w') as f:
        f.write(zshrc_content)

    try:
        os.rename(os.path.join(home, '.zshrc-symlink'),
                  os.path.join(home, '.zshrc-symlink.bak'))
    except OSError:
        pass

    os.symlink(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '.zshrc'),
        os.path.join(home, '.zshrc-symlink'))


def setup_glab_scripts():
    if input('Add glab scripts to PATH? (yes/no) ') not in yes_answers:
        return

    if system == 'Windows':
        print('You are running Windows - glab scripts cannot be setup')
        return

    with open(os.path.join(home, '.zshrc'), 'a') as f:
        f.write(f'export PATH="$PATH:{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gitlab')}"\n')


def main():
    setup_bashrc()
    setup_zshrc()
    setup_git()
    setup_glab_scripts()


if __name__ == '__main__':
    main()
