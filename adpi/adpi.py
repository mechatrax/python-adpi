from time import sleep
from .ADC.AD779x import AD7794
from .EEPROM.AT24 import AT24C256
from .GPIO.MCP230xx import MCP23008

class ADPiPro():
    def __init__(self, spi, i2c, eeprom_addr=0x57, gpio_addr=0x27):
        self.adc = AD7794(spi)
        self.eeprom = AT24C256(i2c, eeprom_addr)
        self.gpio = MCP23008(i2c, gpio_addr)
        self.channels = 4

    def reset(self):
        self.adc.reset()
        sleep(0.0005)

    def read_status(self):
        return self.adc.read_data(self.adc.register['status'])

    def read_mode(self):
        return self.adc.read_bytes(self.adc.register['mode'])

    def write_mode(self, mode, rate):
        self.adc.write_bytes(self.adc.register['mode'], [mode, rate])
    
    def read_configuration(self):
        return self.adc.read_bytes(self.adc.register['configuration'])
    
    def write_configuration(self, gain, ch):
        self.adc.write_bytes(self.adc.register['configuration'], [gain, ch])

    def read_data(self):
        return self.adc.read_data(self.adc.register['data'])

    def read_id(self):
        return self.adc.read_data(self.adc.register['id'])

    def read_offset(self):
        return self.adc.read_data(self.adc.register['offset'])

    def write_offset(self, val):
        self.adc.write_data(self.adc.register['offset'], val)

    def read_fullscale(self):
        return self.adc.read_data(self.adc.register['fullscale'])

    def write_fullscale(self, val):
        self.adc.write_data(self.adc.register['fullscale'], val)

    def load_bias(self, idx):
        dat = self.eeprom.read(32 * idx)
        val = []
        for i in range(4):
            val.append(0)
            for j in range(4):
                val[i] += dat[4 * i + j] << (8 * j)
        return val
    
    def save_bias(self, idx, val):
        dat = []
        for v in val:
            for i in range(4):
                dat.append((v >> (8 * i)) & 0xFF)
        self.eeprom.write(32 * idx, dat)
        sleep(0.005)
    
    def load_scale(self, idx):
        dat = self.eeprom.read(32 * idx + 16)
        val = []
        for i in range(4):
            val.append(0)
            for j in range(4):
                val[i] += dat[4 * i + j] << (8 * j)
        return val
    
    def save_scale(self, idx, val):
        dat = []
        for v in val:
            for i in range(4):
                dat.append((v >> (8 * i)) & 0xFF)
        self.eeprom.write(32 * idx + 16, dat)
        sleep(0.005)
   
    def get_output(self, idx):
        olat = self.gpio.read(self.gpio.register['olat'])
        return (olat >> idx) & 0x01
	
    def set_output(self, idx, val):
        olat = self.gpio.read(self.gpio.register['olat'])
        if val:
            olat |= 0x01 << idx
        else:
            olat ^= 0x01 << idx
        self.gpio.write(self.gpio.register['iodir'], 0xF0)
        self.gpio.write(self.gpio.register['olat'], olat)

