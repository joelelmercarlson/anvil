# anvil
ImageFactory

All you need is a bootable iso and a customization script to make
all your dreams come true!

## Usage

```
usage: example.py [-h] [-n IMAGENAME] [-i ISO] [-o OVFTOOL] [-p PACKER]
                  [-s SCRIPT]

optional arguments:
  -h, --help            show this help message and exit
  -n IMAGENAME, --imagename IMAGENAME
                        rhel-8-3-0
  -i ISO, --iso ISO     file:///var/tmp/rhel-8-3-0-baseos-x86_64-v2020.11.20.i
                        so
  -o OVFTOOL, --ovftool OVFTOOL
                        /bin/ovftool
  -p PACKER, --packer PACKER
                        /usr/local/bin/packer
  -s SCRIPT, --script SCRIPT
                        file:///var/tmp/rhel-8-3-0.sh
```

## Automation Software

- VMware Workstation
- packer
- mkisofs

## Author

"Joel E Carlson" &lt;joel.elmer.carlson@gmail.com&gt;
