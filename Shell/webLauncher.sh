#!/bin/sh
# webLauncher.sh

vncserver
cd mjpg-streamer
sudo ./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"

