#!/usr/bin/python3

from base import *


class PipPackage(BasePackage):
    def __init__(self, name):
        super().__init__(name)

    def check_installed(self):
        installed = run(['pip3', 'list'])
        return self.name in installed

    def do_update(self):
        run(['pip3', 'install', '--upgrade', self.name])

    def do_install(self):
        run(['pip3', 'install', self.name])

