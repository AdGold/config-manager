#!/usr/bin/python3

from base import *
from apt_package import AptPackage

git = AptPackage('git')


class GitPackage(BasePackage):
    GIT_CLONE_DIR = '/home/adrian/.git_installs'
    def __init__(self, name, cmds=[], dir=''):
        self.user, sname = name.split('/')
        super().__init__(sname)
        self.url = 'https://github.com/%s.git' % name
        self.url = 'git@github.com:%s.git' % name
        self.install_dir = dir or self.GIT_CLONE_DIR
        self.full_path = os.path.join(self.install_dir, self.name)
        self.install_cmds = cmds if isinstance(cmds, list) else [cmds]

    def check_installed(self):
        return os.path.exists(self.full_path)

    def do_install(self):
        if not git.check_installed():
            git.install()
        run(['mkdir', '-p', self.install_dir])
        os.chdir(self.install_dir)
        run(['git', 'clone', self.url])
        os.chdir(self.full_path)
        self.do_install_cmds()

    def do_update(self):
        if not git.check_installed():
            git.install()
        os.chdir(self.full_path)
        curr_hash = run('git rev-parse HEAD')
        run(['git', 'pull'])
        new_hash = run('git rev-parse HEAD')
        if curr_hash != new_hash:
            self.do_install_cmds()

    def do_install_cmds(self):
        for cmd in self.install_cmds:
            run(cmd)


