##~---------------------------------------------------------------------------##
##                        ____                       _   _                    ##
##                  _ __ |___ \ ___  _ __ ___   __ _| |_| |_                  ##
##                 | '_ \  __) / _ \| '_ ` _ \ / _` | __| __|                 ##
##                 | | | |/ __/ (_) | | | | | | (_| | |_| |_                  ##
##                 |_| |_|_____\___/|_| |_| |_|\__,_|\__|\__|                 ##
##                              www.n2omatt.com                               ##
##  File      : run_lhc.py                                                    ##
##  Project   : sublimetext3_config                                           ##
##  Date      : Oct 27, 2017                                                  ##
##  License   : GPLv3                                                         ##
##  Author    : n2omatt <n2omatt@amazingcow.com                               ##
##  Copyright : n2omatt - 2017                                                ##
##                                                                            ##
##  Description :                                                             ##
##                                                                            ##
##---------------------------------------------------------------------------~##

################################################################################
## Imports                                                                    ##
################################################################################
## Sublime
import sublime;
import sublime_plugin;
## Python
import os;
import os.path;

################################################################################
## Script                                                                     ##
################################################################################
class RunLicenseHeaderCheckerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = os.path.abspath(self.view.file_name());
        os.system(
            "cd {0} && lhc {1} > /home/n2omatt/Desktop/log.txt".format(
                os.path.dirname(filepath),
                filepath
            )
        );

