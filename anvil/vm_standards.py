# -*- coding:utf-8 -*-

# pylint: disable=C0301

"""
vm_standards -- production settings for vmware
"""
from collections import defaultdict

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]


def vm_standard(vmname):
    """
    default template.json

    :param vmname: str
    """
    ks_settings = ks_boot()
    vm_settings = vmware_settings(vmname)
    vmx_settings = vmx()
    data = {**ks_settings, **vm_settings}
    data = {**data, **vmx_settings}
    return data


def ks_boot():
    """
    kickstart boot for centos/rhel

    :returns: dict
    """
    data = defaultdict(list)
    data['boot_command'].append('<esc><wait>')
    data['boot_command'].append('vmlinuz initrd=initrd.img inst.geoloc=0 rd.driver.blacklist=dm-multipath net.ifnames=0 biosdevname=0 ')
    data['boot_command'].append('<enter>')
    return data


def vmware_settings(vmname):
    """
    vmware settings

    :param vmname: str
    :param ostype: str
    :returns: dict
    """
    standards = {}
    standards['vm_name'] = vmname
    standards['guest_os_type'] = 'rhel8-64'
    standards['boot_wait'] = '15s'
    standards['disk_size'] = '102400'
    standards['disk_type_id'] = 0
    standards['version'] = '17'
    standards['headless'] = 'true'
    standards['http_directory'] = 'http'
    standards['ssh_wait_timeout'] = '25m'
    standards['shutdown_command'] = "echo 'rmdir --ignore-fail-on-non-empty /tmp/*' > /tmp/shutdown.sh;echo '/sbin/halt -h -p' >> /tmp/shutdown.sh; echo 'packer'|sudo -S sh '/tmp/shutdown.sh'"
    standards['output_directory'] = 'output-vmware-iso'
    standards['memory'] = 4096
    standards['cpus'] = 2
    return standards


def vmx():
    """
    vmx settings

    :returns: dict
    """
    data = {}
    standards = {}
    standards['tools.upgrade.policy'] = 'manual'
    standards['disk.EnableUUID'] = 'true'
    standards['ethernet0.present'] = 'true'
    standards['ethernet0.startConnected'] = 'true'
    standards['tools.syncTime'] = 0
    standards['time.synchronize.continue'] = 0
    standards['time.synchronize.restore'] = 0
    standards['time.synchronize.resume.disk'] = 0
    standards['time.synchronize.shrink'] = 0
    standards['time.synchronize.tools.startup'] = 0
    standards['time.synchronize.tools.enable'] = 0
    standards['time.synchronize.resume.host'] = 0
    data['vmx_data'] = standards
    return data
