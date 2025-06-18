from Xlib.display import Display
import time

d = Display()
r = d.screen().root

while True:
    r.warp_pointer(1980, 720); d.flush()
    time.sleep(0.01)
    r.warp_pointer(1380, 900); d.flush()
    time.sleep(0.01)
