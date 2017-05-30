import machine
import time

pin = machine.Pin(2,machine.Pin.OUT)

while True:
    pin.value(not pin.value())
    time.sleep_ms(500)


