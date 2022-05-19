# DVL A50 ROS2, CTD + other

initial version

## create another package

cd ~/dev_ws/src
ros2 pkg create --build-type ament_python <package_name>

## developed in

Distributor ID: Ubuntu
Description:    Ubuntu 20.04.4 LTS
Release:        20.04
Codename:       focal

ros2 foxy

requires in raspberry pi netplan yaml something like this:
```
# This file is generated from information provided by the datasource.  Changes
# to it will not persist across an instance reboot.  To disable cloud-init's
# network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
    version: 2
    ethernets:
        eth0:
            dhcp4: no
            addresses:
```


# add new ros package 

for python 
ros2 pkg create --build-type ament_python <package_name>

## known issues

- publisher only
- fixed ip address - tested in ubuntu 20.04 desktop thinkpad and raspberry pi 4 
- no proper error handling
- handles only dvl messages, no TS messages