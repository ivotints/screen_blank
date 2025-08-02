from Xlib.display import Display
from Xlib import X, XK
from Xlib.ext import xtest
import time

d = Display()
r = d.screen().root

# Get keycode for F13
f13_keycode = d.keysym_to_keycode(XK.string_to_keysym('F13'))

last_f13 = time.time()

while True:
    r.warp_pointer(1980, 720); d.flush()
    time.sleep(0.01)
    r.warp_pointer(1380, 900); d.flush()
    time.sleep(0.01)

    # Every 4 minutes, send F13 key press/release
    if time.time() - last_f13 > 240:
        xtest.fake_input(d, X.KeyPress, f13_keycode)
        xtest.fake_input(d, X.KeyRelease, f13_keycode)
        d.sync()
        last_f13