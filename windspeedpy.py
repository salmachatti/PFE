import time
from gpiozero import Button
from signal import pause
import statistics
import pyrebase

wind_speed_sensor = Button(5)
wind_count = 0

interval = 3

def spin():
    global wind_count
    wind_count = wind_count + 1
    #print("spin" + str(wind_count))

#time shall be in seconds 
def calc_speed(spins, interval):
    #based on Davis tech document
    # V = P*(2.25/T) the speed is in MPh
    # P = no. of pulses per sample period
    # T = sample period in seconds
    wind_speed_mph = spins * (2.25 / interval) 
    return wind_speed_mph

''' def reset_wind():
    global wind_count
    wind_count = 0 '''

store_speeds = []

wind_speed_sensor.when_pressed = spin

while True:
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
        #print('Global count: ', wind_count)
        #reset_wind()
    #Measure for 10-min
    #bws_10_min = calc_speed(wind_count, 600)
    #print('###### 10-min data #####')
    #print('Global count: ', wind_count)
    #print('10-min BWS: ', bws_10_min)
    #print('##### 10-min END #####')
    #reset_wind()

#pause()
