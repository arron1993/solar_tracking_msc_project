import spidev
from math import pow

class Voltmeter:
    def __init__(self,channel):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.channel = int(channel)
        self.MAX_VOLTAGE = 5
        self.ADC_BITS = 12
        self.ADC_MAX_READING = pow(2,self.ADC_BITS) - 1

    def read_channel(self):
        adc = self.spi.xfer2([1,(8+self.channel)<<4,0])
        data = ((adc[1]&15) << 8) + adc[2]
        print("DATA: ",data)
        return data

    def read_channel_test(self):
        adc = self.spi.xfer2([6+((4&self.channel)>>2),(3&self.channel)<<6,0])
        data = ((adc[1]&15) << 8) + adc[2]
        return data     

    def convert_reading(self, data,places):
        volts = (data * 5) / float(4095)
        volts = round(volts,places)
        return volts
     
    def get_voltage(self):
        raw_data = self.read_channel_test()
        voltage = self.convert_reading(raw_data,4)
        return voltage
