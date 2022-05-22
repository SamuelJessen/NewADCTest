import board
import digitalio
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)

adsforceGND = ADS.ADS1015(address=48,i2c=i2c,gain=2/3)
adstemplightVCC = ADS.ADS1015(address=49,i2c=i2c,gain=2/3)

chanforce = AnalogIn(adsforceGND, ADS.P0)
chanlight = AnalogIn(adstemplightVCC, ADS.P0)


while True:
    print("Force adc (GND):" + str(chanforce.value), str(chan.voltage))
    print("Light adc (VCC):" + str(chanlight.value), str(chanlight.voltage))


