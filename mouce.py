from Xlib.display import Display

d = Display()
r = d.screen().root

while True:
    r.warp_pointer(1080, 720); d.flush()
    r.warp_pointer(1080,   700); d.flush()
