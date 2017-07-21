#!/usr/bin/python3

import json
import sys
import os

from base import BasePackage
from git_package import GitPackage
from pip_package import PipPackage
from apt_package import AptPackage
from custom_package import CustomPackage

types = {
    'git':GitPackage,
    'apt':AptPackage,
    'pip':PipPackage,
    'custom':CustomPackage,
}

def parse(d):
    if isinstance(d, dict):
        if 'type' in d:
            t = types[d['type']]
            del d['type']
            return t(**d)
        return {k:parse(v) for k,v in d.items()}
    elif isinstance(d, list):
        return [parse(x) for x in d]

failed = []
def install(d, depth=0):
    if isinstance(d, dict):
        for k,v in d.items():
            print(' '*depth + 'Installing', k)
            install(v, depth+1)
    elif isinstance(d, list):
        for v in d:
            install(v, depth+1)
    elif isinstance(d, BasePackage):
        if not d.install():
            failed.append(d.name)

config = json.load(open(sys.argv[1]))

packages = parse(config)

os.system('sudo sed -i.bak "/^# deb .*partner/ s/^# //" /etc/apt/sources.list')

install(packages)
print('Failed packages')
for f in failed:
    print(f)
