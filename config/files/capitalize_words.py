##----------------------------------------------------------------------------##
## File      : capitalize_words.py                                            ##
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
class CapitalizeWordsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();
        for s in sel:
            value_str = self.view.substr(s);
            self.view.replace(
                edit,
                s,
                value_str.capitalize()
            );
