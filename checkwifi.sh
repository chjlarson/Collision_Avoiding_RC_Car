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
