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


################################################################################
## Constants                                                                  ##
################################################################################
WHO_AM_I="$(whoami)";

OSX_PATH="$HOME/Library/Application Support/Sublime Text 3/Packages/User/"
LINUX_PATH="$HOME/.config/sublime-text-3/Packages/User/";
NT_PATH="/cygdrive/c/Users/$WHO_AM_I/AppData/Roaming/"Sublime\ Text\ 3/Packages/User/;


################################################################################
## Variables                                                                  ##
################################################################################
HOST=$(uname -s);

IS_ON_NT=$( echo $HOST | grep -i cygwin);
IS_ON_OSX=$(echo $HOST | grep -i darwin);

PLATFORM_OPTION="$1";


################################################################################
## Functions                                                                  ##
################################################################################
replace_file_contents()
{
    STR=$1;
    FILE_TO_INSERT=$2
    FILE_TO_MODIFY=$3

    # Only to debug...
    echo "STR            $STR";
    echo "FILE_TO_INSERT $FILE_TO_INSERT";
    echo "FILE_TO_MODIFY $FILE_TO_MODIFY";

    sed -i"BACKUP" -e "/$STR/r $FILE_TO_INSERT" -e "/$STR/d" $FILE_TO_MODIFY;
    rm -f ${FILE_TO_MODIFY}BACKUP;
}


################################################################################
## Script                                                                     ##
################################################################################
## Get any platform options that we may passed.
if [ -z "$PLATFORM_OPTION" ]; then
    PLATFORM_OPTION="default";
fi;

## Clean up the build directory.
rm    -rf build;
mkdir -p  build;

## Log.
echo "--> Installing Sublime Text 3 configuration files...";
echo "----> OS              : ($HOST)";
echo "----> IS_ON_NT        : ($IS_ON_NT)";
echo "----> IS_ON_OSX       : ($IS_ON_OSX)";
echo "----> PLATFORM_OPTION : ($PLATFORM_OPTION)";

## Get the correct path.
FINAL_PATH="";
if [ -n "$IS_ON_NT" ]; then
    FINAL_PATH="$NT_PATH";
elif [ -n "$IS_ON_OSX" ]; then
    FINAL_PATH="$OSX_PATH";
else
    FINAL_PATH="$LINUX_PATH";
fi;

## Copy everything needed to build path.
echo "----> Copying files to build dir";
cp -r ./config/files/* ./build;


## Do the replacements needed to this platform.
if [ ! -e "./config/preferences/$PLATFORM_OPTION.txt" ]; then
    echo "PLATFORM_OPTION ($PLATFORM_OPTION) is not valid - Aborting...";
    exit 1;
fi;

## STR - FILE TO INSERT - FILE TO MODIFY
replace_file_contents "__FONT_CONFIG__"                         \
                      ./config/preferences/$PLATFORM_OPTION.txt \
                      ./build/Preferences.sublime-settings


## Copy everything needed to build path.
echo "----> Copying files to ($FINAL_PATH)";
mkdir -pv "$FINAL_PATH"
cp -Rv ./build/* "$FINAL_PATH";

echo "--> Done...";
