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
  -i ISO, --iso ISO     file:///var/www/html/pub/latest.iso
  -o OVFTOOL, --ovftool OVFTOOL
                        /bin/ovftool
  -p PACKER, --packer PACKER
                        /usr/local/bin/packer
  -s SCRIPT, --script SCRIPT
                        file:///var/www/html/pub/config.sh
```

## Automation Software

&mdash; VMware Workstation

&mdash; packer

&mdash; mkisofs

## Author

&ldquo;Joel E Carlson&rdquo; &lt;joel.elmer.carlson@gmail.com&gt;
