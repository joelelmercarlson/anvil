# -*- coding: utf-8 -*-

"""
create_sandbox.py -- checks environment and prepares for ImageFactory

This program is used as first step to setup ImageFactory execution.
"""
from platform import system
import os
import re
import stat
import sys
import shlex
import subprocess

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']


def check_globals_for_none():
    """
    check_globals_for_none
    """
    for name, value in globals().items():
        match = re.search(r'__.*__', name)
        if not match and value is None:
            print(f'Expected environment variable {name} has no value')
            sys.exit(1)


def check_sudoers():
    """
    check_sudoers

    :returns: bool
    """
    if system() == "Linux":
        return run('sudo -nv')
    return 0


def create(imagename='default'):
    """
    create will create_sandbox and make working directory

    :returns: sandbox
    """
    workspace = os.getenv('WORKSPACE')
    image_name = os.getenv('IMAGE_NAME')
    if workspace is None:
        workspace = '/anvil/run'
    if image_name is None:
        image_name = imagename
    build_path = f'{os.getcwd()}/{workspace}'
    yaml_file = f'{build_path}/{image_name}.yaml'
    playbook_file = f'{build_path}/{image_name}.sh'
    json_file = f'{build_path}/{image_name}.json'
    create_workspace(build_path)
    os.chdir(build_path)
    check_sudoers()
    touch(yaml_file)
    touch(playbook_file)
    touch(json_file)
    return build_path


def run(command):
    """
    run command

    :params command: str
    :returns: int
    """
    process = subprocess.run(shlex.split(command), check=True)
    return process


def touch(filename, times=None):
    """
    touch file
    """
    with open(filename, 'a'):
        os.utime(filename, times)
        set_perms(filename)


def create_workspace(path='/var/tmp'):
    """
    create_workspace

    :params path: str
    """
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'Existing workspace {path}')


def set_perms(filename):
    """
    set_perms

    :params filename: str
    """
    status = os.stat(filename)
    os.chmod(filename, status.st_mode | stat.S_IRGRP | stat.S_IROTH)
