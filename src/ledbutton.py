from machine import Pin



def run():
    print ('Digital Pin I/O')
    led = Pin(2,Pin.OUT)

    button = Pin(4, Pin.PULL_UP)

    while 1:
        state = button.value()
        if state == 0:
            led.on()
        else:
            led.off()
