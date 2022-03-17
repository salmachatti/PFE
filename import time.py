import time
from gpiozero import Button
from signal import pause
import statistics
import pyrebase
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
wind_speed_sensor = Button(5)
wind_count = 0

interval = 3

def spin():

    global wind_count
    wind_count = wind_count + 1
def calc_speed(spins, interval):
    wind_speed_mph = spins * (2.25 / interval) 
    return wind_speed_mph
    store_speeds = []

wind_speed_sensor.when_pressed = spin

while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    data = {"temperature":temperature}
    time.sleep(10)
    start_time = time.time()
    print('##### 10-min started #####')
    while time.time() - start_time <= 600:    
        print('Start 3 second')
        count_start = wind_count
        time.sleep(3)
        count_end = wind_count
        spins = count_end - count_start
        bws_3_sec = calc_speed(spins, 3)
        data_3sec = {
            "bws-3-sec": bws_3_sec,
            
            "timestamp": time.time()
            }
        print('Number of spins: ', spins)
        print('Wind speed (mph): ', bws_3_sec)
    

