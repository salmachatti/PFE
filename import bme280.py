import time
from gpiozero import Button
from signal import pause
import statistics
import pyrebase
import bme280
import time
from w1thermsensor import W1ThermSensor

#variables

sensor = W1ThermSensor()
wind_speed_sensor = Button(5)
wind_count = 0
interval = 3

#functions

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
    time.sleep(5)

    count_start = wind_count
    time.sleep(3)
    count_end = wind_count
    spins = count_end - count_start
    bws_3_sec = calc_speed(spins, 3)
    data_3sec = {
            "bws-3-sec": bws_3_sec,
            "timestamp": time.time()
            }

    print("temperature Sensor")
    print("The temperature is %s celsius" % temperature)

    print('Anemometer Sensor')
    print('Number of spins: ', spins)
    print('Wind speed (mph): ', bws_3_sec)
    (chip_id, chip_version) = bme280.readBME280ID()
    print ("Chip ID :", chip_id)
    print ("Version :", chip_version)
    temperature,pressure,humidity = bme280.readBME280All()
    print ("Temperature : ", temperature, "C")
    print ("Pressure : ", pressure, "hPa")
    print ("Humidity : ", humidity, "%")
    time.sleep(10)