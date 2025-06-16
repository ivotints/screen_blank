from Xlib.display import Display
import time

d = Display()
r = d.screen().root

while True:
    r.warp_pointer(1080, 720); d.flush()
    r.warp_pointer(1080,   700); d.flush()
    time.sleep(0.01)
