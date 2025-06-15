#!/usr/bin/env python3
# press-super-fixed.py — simulate a Super (Windows) key press under X11

from Xlib import X, display, XK
from Xlib.ext import xtest

# open display
d = display.Display()

# look up the keycode for the left Super (Windows) key
kc = d.keysym_to_keycode(XK.XK_Super_L)

# press and release the key
xtest.fake_input(d, X.KeyPress,   kc)
xtest.fake_input(d, X.KeyRelease, kc)

# flush it out to the server
d.sync()
