# -*- coding:utf-8 -*-

# pylint: disable=C0103
# pylint: disable=R0902
# pylint: disable=R0913
# pylint: disable=E0401

"""
:class:`ImageFactory`
"""
import yaml
from . import helpers
from . import create_sandbox

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]


class Anvil():
    """
    :returns: :class:`Anvil`
    """

    def __init__(self, imagename, iso, ovftool, packer, script):
        """
        ImageFactory environment
        """
        self.image_name = imagename
        self.engine = helpers.set_engine(packer)
        self.sandbox = create_sandbox.create(self.image_name)
        self.archiver = helpers.set_archiver(ovftool,
                                             self.sandbox,
                                             self.image_name)
        self.script = helpers.vendor_file(self.sandbox, script)
        self.iso = helpers.vendor_file(self.sandbox, iso)
        self.vm_cfg = helpers.gen_vm_template(self.iso, self.script, self.image_name)
        self.vm_template = helpers.validate_template(self.engine, self.vm_cfg)

    def __repr__(self):
        return (f'Anvil({self.image_name!r}, '
                f'{self.engine!r}, '
                f'{self.sandbox!r}), '
                f'{self.archiver!r}, '
                f'{self.script!r}, '
                f'{self.iso!r}, '
                f'{self.vm_template!r})')

    def archive(self):
        """
        run archiver
        """
        process = create_sandbox.run(self.archiver)
        ova = helpers.get_ova(self.sandbox, self.image_name)
        create_sandbox.set_perms(ova)
        return process

    def checkpoint(self):
        """
        checkpoint saves sandbox files
        """
        kind = f'{self.image_name}.yaml'
        script = f'{self.image_name}.sh'
        vm_template = f'{self.image_name}.json'
        helpers.write_file(kind, yaml.dump(self))
        helpers.write_file(script, helpers.read_file(self.script))
        helpers.write_file(vm_template, self.vm_template)

    def run_vm(self):
        """
        run_vm engine

        :returns: str
        """
        return helpers.run(self.engine, self.vm_template)

    @staticmethod
    def fetch_vm_template(iso, script, vmname):
        """
        fetch_vm_template

        :returns: :class:`json`
        """
        return helpers.gen_vm_template(iso, script, vmname)
