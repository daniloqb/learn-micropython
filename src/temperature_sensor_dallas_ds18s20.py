from __future__ import print_function

import machine, time
import onewire, ds18x20


dat = machine.Pin(12)

ds = ds18x20.DS18X20(onewire.OneWire(dat))

roms = ds.scan()

print ('found devices: ',roms)

while True:
    print('temperatures:',end = ' ')
    ds.convert_temp()
    time.sleep_ms(1000)
    for rom in roms:
        print(ds.read_temp(rom), end=' ')
    print()

