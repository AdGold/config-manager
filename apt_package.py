#!/usr/bin/python3

from base import *


class AptPackage(BasePackage):
    def __init__(self, name, repository='', key=''):
        super().__init__(name)
        self.repository = repository
        self.key = key

    def check_installed(self):
        try:
            _ = run(['dpkg', '-l', self.name])
            return True
        except CalledProcessError:
            return False

    def do_repository_add(self):
        if self.key:
            run(['sudo', 'apt-key', 'adv'] + self.key.split())
        if self.repository:
            added = run(['ls', '-r', '/etc/apt/**/*.list'])
            if any(self.name in f for f in added):
                pass
            else:
                run(['sudo', 'apt-add-repository', '-y', self.repository])
                run(['sudo', 'apt-get', 'update'])

    def do_install(self):
        self.do_repository_add()
        run(['sudo', 'apt-get', 'install', '-y', self.name])

    def do_update(self):
        run(['sudo', 'apt-get', 'upgrade', '-y', self.name])

    def uninstall(self):
        run(['sudo', 'apt-get', 'purge', '-y', self.name])
