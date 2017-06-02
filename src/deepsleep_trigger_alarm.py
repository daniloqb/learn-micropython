import machine


rtc = machine.RTC()

rtc.irq(trigger=rtc.ALARM0, wake= machine.DEEPSLEEP)

rtc.alarm(rtc.ALARM0, 10000)

machine.deepsleep()