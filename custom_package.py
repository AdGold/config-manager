#!/usr/bin/python3

from base import *


class CustomPackage(BasePackage):
    def __init__(self, name, cmds):
        super().__init__(name)
        self.install_cmds = cmds if isinstance(cmds, list) else [cmds]

    def check_installed(self):
        return False # can't tell

    def update(self):
        self.uninstall()
        self.install()

    def do_install(self):
        self.do_install_cmds()

    def do_install_cmds(self):
        for cmd in self.install_cmds:
            run(cmd)
