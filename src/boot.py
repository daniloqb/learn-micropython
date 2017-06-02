# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import machine

webrepl.start()
gc.collect()


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print ('woke from a deep sleep.')
else:
    print ('power on hard reset.')