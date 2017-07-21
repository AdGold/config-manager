#!/usr/bin/python3

import os
from subprocess import CalledProcessError, check_output, STDOUT

DEBUG = True

def run(cmd, *args, **kwargs):
    if isinstance(cmd, str):
        cmd = cmd.split()
    if cmd[0] == 'cd':
        os.chdir(cmd[1])
        return ''
    else:
        #  kwargs['stderr'] = STDOUT
        return check_output(cmd, *args, **kwargs).decode('utf8')

class BasePackage:
    def __init__(self, name):
        self.name = name
        self._log = []

    def log(self, msg):
        if DEBUG:
            print(msg)
        self._log.append(msg)

    def check_installed(self):
        raise NotImplementedError

    def install(self):
        if self.check_installed():
            self.log('Package %s already installed, updating' % self.name)
            return self.update()
        self.log('Installing package %s' % self.name)
        try:
            self.do_install()
        except Exception as ex:
            self.log('Error on package %s: %s' % (self.name, ex))
            return False
        else:
            # self.log('Successfully installed package %s' % self.name)
            return True

    def update(self):
        if not self.check_installed():
            self.log('Package %s not already installed, installing' % self.name)
            return self.install()
        self.log('Updating package %s' % self.name)
        try:
            self.do_update()
        except Exception as ex:
            self.log('Error on package %s: %s' % (self.name, ex))
            return False
        else:
            self.log('Successfully updated package %s' % self.name)
            return True

    def do_install(self):
        raise NotImplementedError

    def do_update(self):
        raise NotImplementedError

    def uninstall(self):
        raise NotImplementedError
