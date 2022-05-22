import time
import os
import glob
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#regarding temperature:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
adsforce = ADS.ADS1015(i2c=i2c,gain=2/3, address=0x48)
adslight = ADS.ADS1015(i2c=i2c,gain=2/3, address=0x49)

# Create single-ended input on channel 0
forceread = AnalogIn(adsforce, ADS.P0)
lightread = AnalogIn(adslight, ADS.P0)

#print("{:>5}\t{:>5}".format("raw", "v"))

while True:
    print("Voltage read from force:" + str(forceread.voltage))
    print("Voltage read from light:" + str(lightread.voltage))
    print("Temperature: " + str(read_temp()))	
    time.sleep(1)
