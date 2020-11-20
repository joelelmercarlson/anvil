# -*- coding: utf-8 -*-

# pylint: disable=E0401

"""
ImageFactory helpers.py
"""
from collections import defaultdict
import hashlib
import json
import os
import sys
import re
import wget
from packerpy import PackerExecutable
from .vm_standards import vm_standard

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]


def check_file(filename):
    """
    check_file for existence

    :param filename: str
    """
    status = 0
    try:
        status = os.stat(filename)
    except FileNotFoundError:
        print(f'no such {filename}: status={status}')
        sys.exit(1)


def gen_vm_template(iso, script, vmname):
    """
    gen_vm_template

    :param iso: str
    :param script: str
    :param vmname: str
    :returns: :class:`json`
    """
    check_file(iso)
    check_file(script)
    with open(iso, 'rb') as stream:
        contents = stream.read()
    message = hashlib.md5(contents).hexdigest()
    builder = set_vm_builders(iso, message, vmname)
    provisioner = set_provisioners(script)
    template = {**builder, **provisioner}
    return json.dumps(template)


def read_file(filename):
    """
    read_file

    :param filename: str
    :returns: str
    """
    contents = ''
    with open(filename, 'r') as stream:
        contents = stream.read()
    return contents


def run(packer, template):
    """
    run the build

    :param packer: :class:`packerpy`
    :param template: str
    """
    (ret, out, err) = packer.build(template,
                                   force=True,
                                   color=True,
                                   on_error='cleanup')
    if ret != 0:
        print(f'packer build: ret={ret}, out={out}, err={err}')
        sys.exit()
    return (ret, out, err)


def set_vm_builders(iso, checksum, vmname):
    """
    set_vm_builders -- integrate builders

    :param iso: str
    :param checksum: str
    :param vmname: str
    :returns: dict
    """
    builders = defaultdict(list)
    builder = {'type': 'vmware-iso',
               'iso_url': 'file://' + iso,
               'iso_checksum': checksum,
               'ssh_username': 'packer',
               'ssh_password': 'packer',
               'shutdown_command': 'sudo poweroff -f'}
    vmware = vm_standard(vmname)
    builder = {**builder, **vmware}
    builders['builders'].append(builder)
    return builders


def set_provisioners(script):
    """
    set_template -- integrate provisioners

    :param script: str
    :returns: dict
    """
    provisioners = defaultdict(list)
    provisioner = {'script': script,
                   'type': 'shell'}
    provisioners['provisioners'].append(provisioner)
    return provisioners


def set_engine(packer='/usr/local/bin/packer'):
    """
    packer binary -- full path, check perms, so on...

    :param packer: str
    :returns: :class:`packerpy`
    """
    return PackerExecutable(packer)


def set_archiver(ovftool='/bin/ovftool', path='/var/tmp', image='default'):
    """
    ovftool binary -- full path, perms, so on...

    :param ovftool: str
    :param path: str
    :param image: str
    :returns: str
    """
    out = 'output-vmware-iso'
    vmx = f'{path}/{out}/{image}.vmx'
    ova = f'{path}/{out}/{image}.ova'
    ovf_tool = f"""{ovftool} \
    --X:logFile={path}/debug_layer1.log \
    --X:logLevel=verbose \
    --maxVirtualHardwareVersion=13 \
    --shaAlgorithm=sha256 \
    {vmx} {ova}"""
    return ovf_tool


def validate_template(packer, template):
    """
    validate_template

    :param packer: :class:`packerpy`
    :param template: str"""
    (ret, out, err) = packer.validate(template)
    if ret != 0:
        print(f'packer validate: ret={ret}, out={out}, err={err}')
        sys.exit(1)
    return template


def vendor_file(sandbox, url):
    """
    vendor_file

    :param sandbox: str
    :param url: str
    :returns: str
    """
    match = re.search(':', url)
    if not match:
        url = f'file://{url}'
    filename = wget.download(url)
    check_file(filename)
    return f'{sandbox}/{filename}'


def write_file(filename, contents):
    """
    write_file

    :param filename: str
    :param contents: str
    """
    with open(filename, 'w') as stream:
        stream.write(contents)
