#!/bin/bash
################################################################################
## File    : install.sh                                                       ##
## Project : sublimetext3_config                                              ##
## Date    : May 22, 2017                                                     ##
## Author  : n2omatt@amazingcow.com                                           ##
## License : GPLv3                                                            ##
##                                                                            ##
## Description :                                                              ##
##   Install the sublime configuration :D                                     ##
################################################################################


## Constants...
WHO_AM_I="$(whoami)";

OSX_PATH="$HOME/Library/Application Support/Sublime Text 3/Packages/User/"
LINUX_PATH="$HOME/.config/sublime-text-3/Packages/User/";
NT_PATH=/cygdrive/c/Users/matt/AppData/Roaming/Sublime\ Text\ 3/Packages/User/;

## Variables..
HOST=$(uname -s);

IS_ON_NT=$( echo $HOST | grep -i cygwin);
IS_ON_OSX=$(echo $HOST | grep -i darwin);

echo "--> Installing Sublime Text 3 configuration files...";
echo "----> OS        : ($HOST)";
echo "----> IS_ON_NT  : ($IS_ON_NT)";
echo "----> IS_ON_OSX : ($IS_ON_OSX)";

## Copy the configuration to the correct path.
if [ -n "$IS_ON_NT" ]; then
    echo "----> Copying files to ($NT_PATH)";
    cp -Rv ./config/* "$NT_PATH";
elif [ -n "$IS_ON_OSX" ]; then
    echo "----> Copying files to ($OSX_PATH)";
    cp -Rv ./sublime_config/* "$OSX_PATH";
else
    echo "----> Copying files to ($LINUX_PATH)";
    cp -Rv ./sublime_config/* "$LINUX_PATH";
fi;

echo "--> Done...";
