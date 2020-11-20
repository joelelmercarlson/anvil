# -*- coding:utf-8 -*-

"""
pylinter automated

Abstract
========
pylinter utilize pylint on our python.

Requirements
============
| YAML -- file containing what directories to scan.

Example
=======
>>> import pylinter
>>> YAML = 'Manifest.yaml'
>>> RUNLIST = pylinter.loader(YAML)
>>> pylinter.run(RUNLIST)
"""
import os
import re
import yaml

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]


def banner(message):
    """:param message: (str)"""
    counter = len(message)
    rule = "="
    while counter > 0:
        counter -= 1
        rule += "="
    print(message)
    print(rule)


def loader(filename):
    """loader reads file.yaml

    :param filename: (str)
    :returns: contents (yaml)"""
    contents = ''
    with open(filename, 'r') as stream:
        contents = yaml.load(stream, Loader=yaml.FullLoader)
    return contents


def pylint(filename):
    """:param filename: (str)"""
    if filename is None:
        return
    cmd = f'pylint {filename}'
    banner(filename)
    os.system(cmd)


def py_filter(filename):
    """:param filename: (str)
    :returns: match (str)"""
    match = re.search(r'.*.py$', filename)
    if match:
        return match.group()
    return None


def walk(directory):
    """walk a directory w/ pylint

    :param directory: (str)"""
    dir_list = os.listdir(directory)
    files = []
    for i in dir_list:
        path = f'{directory}/{i}'
        filename = py_filter(path)
        files.append(filename)
    for i in files:
        pylint(i)


def run(runlist):
    """run walks the runlist

    :param runlist: (dict)"""
    for value in runlist.values():
        for directory in value:
            walk(directory)


if __name__ == '__main__':
    YAML = 'Manifest.yaml'
    RUNLIST = loader(YAML)
    run(RUNLIST)
