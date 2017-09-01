##----------------------------------------------------------------------------##
## File      : insert_datetime.py                                             ##
## Project   : sublimetext3_config                                            ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : August 30, 2017                                                ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##                                                                            ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
import time;
import sublime;
import sublime_plugin;

################################################################################
## Script                                                                     ##
################################################################################
class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();
        for s in sel:
            self.view.replace(edit, s, time.asctime(time.gmtime()) + " UTC");
