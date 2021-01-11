# anvil
anvil creates VM images in OVA format.

All you need is a bootable iso and a customization script to make
VM images.

## Usage

```
usage: example.py [-h] [-n IMAGENAME] [-i ISO] [-o OVFTOOL] [-p PACKER]
                  [-s SCRIPT]

optional arguments:
  -h, --help            show this help message and exit
  -n IMAGENAME, --imagename IMAGENAME
                        rhel83
  -i ISO, --iso ISO     file:///var/lib/anvil/latest.iso
  -o OVFTOOL, --ovftool OVFTOOL
                        /bin/ovftool
  -p PACKER, --packer PACKER
                        /usr/local/bin/packer
  -s SCRIPT, --script SCRIPT
                        file:///var/lib/anvil/config.sh
```

## Automation Software

&mdash; VMware Workstation

&mdash; packer

&mdash; ovftool

&mdash; mkisofs

## Environment

The filesystem layout for the example.py.

```
/var/lib/anvil
/var/lib/anvil/run
/var/lib/anvil/latest.iso
/var/lib/anvil/config.sh
```

## Author

&ldquo;Joel E Carlson&rdquo; &lt;joel.elmer.carlson@gmail.com&gt;
