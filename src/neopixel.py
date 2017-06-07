import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(4),8)

np[0]  = (255,0,0)
np[1]  = (0,128,0)
np[2]  = (0,0,64)

np.write();