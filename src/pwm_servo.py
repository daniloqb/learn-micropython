import machine, time, math

def pulse(led, delay):
    for i in range(200):
        led.duty(int(math.sin(i/10*math.pi)*500 + 500))
        time.sleep_ms(delay)



led = machine.PWM(machine.Pin(12), freq=50)

led.duty(0)

while True:
    pulse(led,100)