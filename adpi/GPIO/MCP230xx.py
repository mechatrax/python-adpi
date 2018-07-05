class MCP23008():
    register = {
        'iodir':   0x00,
        'ipol':    0x01,
        'gpinten': 0x02,
        'defval':  0x03,
        'intcon':  0x04,
        'iocon':   0x05,
        'gppu':    0x06,
        'intf':    0x07,
        'intcap':  0x08,
        'gpio':    0x09,
        'olat':    0x0A,
    }
    
    def __init__(self, i2c, chipaddr):
        self.i2c = i2c
        self.address = chipaddr

    def read(self, regaddr):
        return self.i2c.read_byte_data(self.address, regaddr)

    def write(self, regaddr, dat):
        self.i2c.write_byte_data(self.address, regaddr, dat)

