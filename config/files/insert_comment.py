##----------------------------------------------------------------------------##
## File      : insert_comment.py                                              ##
## Project   : sublimetext3_config                                            ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : Sep 10, 2017                                                   ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##                                                                            ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
## Python
import time;
import os.path;
## Sublime
import sublime;
import sublime_plugin;

################################################################################
## Constants                                                                  ##
################################################################################
slash_cmt = [
    ## C / C++
    "cpp",
    "c",
    "h",
    "hpp",
    ## ObjC
    "m",
    "mm",
    ## C#
    "cs",
    # Javascript
    "js",
    "jsx",
    ## Action Script
    "as3",
    ## PHP
    "php",
];

hash_cmt = [
    ## Shell
    "sh",
    ## SQL
    "sql",
    ## Python
    "py",
];

other_cmt = {
    "html" : ["<!-- ", "-", " -->"],
    "md" : ["<!-- ", "-", " -->"]
};


################################################################################
## Functions                                                                  ##
################################################################################
def get_start_comment_for_ext(ext):
    ## Extension isn't in any list,
    ##    Check if it is a 'special' extension...
    if(ext in other_cmt.keys()):
        return other_cmt[ext][0];

    ## Check which list is the ext...
    if  (ext in slash_cmt): return "/";
    elif(ext in hash_cmt ): return "#";

    ## Can't find the ext...
    ##    Probally a script file without ext...
    return "#";

def get_end_comment_for_ext(ext):
    ## Extension isn't in any list,
    ##    Check if it is a 'special' extension...
    if(ext in other_cmt.keys()):
        return other_cmt[ext][2];

    return get_start_comment_for_ext(ext);

def get_middle_comment_for_ext(ext):
    return "-";


def fill(start, middle, end, content):
    real_start  = start if len(start) != 1 else start * 2;
    real_end    = end   if len(end  ) != 1 else end   * 2;
    real_middle = middle * (80 - len(real_end) - len(real_start));

    ## Build line 1 and 3.
    line1_3 = real_start + real_middle + real_end;

    ## Build line 2.
    start_spc = "" if real_start[-1] == " " else " "; ## Put spaces only if needed.
    line_2  = real_start + start_spc + content; ## Build first part...
    line_2 += " " * (80 - len(real_end) - len(line_2)) + real_end;

    return "{0}\n{1}\n{0}".format(line1_3, line_2);


################################################################################
## Script                                                                     ##
################################################################################
class InsertCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view     = sublime.active_window().active_view();
        filename = view.file_name();
        ext      = os.path.splitext(filename)[1];

        ## Clean the dot...
        ext = ext.replace(".", "");

        ## Get what we gonna put on comment..
        sel     = self.view.sel()[0];
        content = view.substr(sel);

        comment = fill(
            get_start_comment_for_ext (ext),
            get_middle_comment_for_ext(ext),
            get_end_comment_for_ext   (ext),
            content
        );

        ## Save the current "cursor" position on the buffer.
        ##   It'll be used in case that we don't have nothing
        ##   select as content, so we get the cursor at the
        ##   position to insert a string...
        pos = view.sel()[0];

        self.view.replace(edit, sel, comment);

        self.view.sel().clear();
        self.view.sel().add(
            sublime.Region(
                pos.a + 84, ##COWTODO(n2omatt): Remove magic numbers...
                pos.a + 90
            )
        );



