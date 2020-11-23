# packages
sudo dnf -y install libnsl libXcursor-devel kernel-devel libXtst-devel libXinerama-devel unzip

# packer
curl -O https://releases.hashicorp.com/packer/1.6.5/packer_1.6.5_linux_amd64.zip
unzip packer_1.6.5_linux_amd64.zip
sudo cp packer /usr/local/bin/

# software
sudo /bin/sh VMware-Workstation-Full-16.1.0-17198959.x86_64.bundle \
--console \
--eulas-agreed \
--set-setting vmware-workstation serialNumber YOUR_KEY \
--set-setting vmware-player-app softwareUpdateEnabled no
