#!/bin/bash
#checkwifi.sh
#The Raspberry Pi does not automatically reconnect to a known network if the connection is lost.
#This script checks to see if the Raspberry Pi can still communicate with the default gateway.
#This script does not take into account the situation where the defualt gateway is down instead of the Raspberry Pi causing
#  the loss of the connection. In that event, the Raspberry Pi will continuesly restart its network until the connection is reestablished.

ping -c4 192.168.69.69 > /dev/null
 
if [ $? != 0 ] 
then
  ping -c4 172.20.10.1 > /dev/null
  if [ $? != 0 ]
  then
    echo "No network connection, restarting wlan0"
    /sbin/ifdown 'wlan0'
    sleep 5
    /sbin/ifup --force 'wlan0'
  fi
fi
