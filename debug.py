# Copyright © 2014 Bart Massey
# Print iff debugging is true.

from sys import stderr

debug_mode = False

def set_debug():
    global debug_mode
    debug_mode = True

def clear_debug():
    global debug_mode
    debug_mode = False

def debugging():
    return debug_mode

def debug(*args, **kwargs):
    if debug_mode:
        kwargs["file"] = stderr
        print(*args, **kwargs)
