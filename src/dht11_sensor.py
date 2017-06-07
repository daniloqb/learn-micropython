import machine
import dht
import time

sensor = dht.DHT11(machine.Pin(4))


while True:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()

    print('Temperature: %d Humidity: %d%%' %(t,h))
    time.sleep_ms(1500)

