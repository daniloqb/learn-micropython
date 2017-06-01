import machine, time, math

def pulse(led, delay):
    for i in range(20):
        led.duty(int(math.sin(i/10*math.pi)*500 + 500))
        time.sleep_ms(delay)



led = machine.PWM(machine.Pin(2), freq=1000)

while True:
    pulse(led,50)

