# -*- coding:utf-8 -*-

"""
example.py -- ImageFactory in action
"""
import argparse
import anvil

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]

IMAGENAME = 'rhel83'
ISO = 'file:///var/lib/anvil/latest.iso'
OVFTOOL = '/bin/ovftool'
PACKER = '/usr/local/bin/packer'
SCRIPT = 'file:///var/lib/anvil/config.sh'


def get_arguments():
    """
    get_arguments for cli

    :returns: parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--imagename', help=IMAGENAME)
    parser.add_argument('-i', '--iso', help=ISO)
    parser.add_argument('-o', '--ovftool', help=OVFTOOL)
    parser.add_argument('-p', '--packer', help=PACKER)
    parser.add_argument('-s', '--script', help=SCRIPT)
    return parser.parse_args()


def run():
    """
    run
    """
    # what do you want to do?
    resp = {}
    resp['imagename'] = IMAGENAME
    resp['iso'] = ISO
    resp['ovftool'] = OVFTOOL
    resp['packer'] = PACKER
    resp['script'] = SCRIPT

    # cli
    args = get_arguments()
    resp['imagename'] = args.imagename or resp['imagename']
    resp['iso'] = args.iso or resp['iso']
    resp['ovftool'] = args.ovftool or resp['ovftool']
    resp['packer'] = args.packer or resp['packer']
    resp['script'] = args.script or resp['script']

    print('Strike the Anvil...')
    image = anvil.Anvil(resp['imagename'],
                        resp['iso'],
                        resp['ovftool'],
                        resp['packer'],
                        resp['script'])
    image.checkpoint()

    print('\n')
    print('Forge the Image...')
    ret, out, err = image.run_vm()

    print('See the Results...')
    print(ret, out.decode('utf-8'), err)

    print('Package the VM...')
    ret2 = image.archive()
    print(ret2)

    print('All Done!')

if __name__ == '__main__':
    run()
