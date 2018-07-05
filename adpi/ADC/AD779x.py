class AD7794():
    mode = {
        'continuous':   0x00,
        'single':       0x20,
        'idle':         0x40, 
        'powerdown':    0x60,
        'cal_int_zero': 0x80,
        'cal_int_full': 0xA0,
        'cal_sys_zero': 0xC0,
        'cal_sys_full': 0xE0
    }
    gain = {
        '1':   0,
        '2':   1,
        '4':   2,
        '8':   3,
        '16':  4,
        '32':  5,
        '64':  6,
        '128': 7,
    }
    channel = {
        '1':    0x00,
        '2':    0x01,
        '3':    0x02,
        '4':    0x03,
        'temp': 0x06,
    }
    rate = {
        '470': 0x01,
        '242': 0x02,
        '123': 0x03,
        '62':  0x04,
        '50':  0x05,
        '39':  0x06,
        '33':  0x07,
        '19':  0x08,
        '17':  0x09,
        '16':  0x0A,
        '12':  0x0B,
        '10':  0x0C,
        '8':   0x0D,
        '6':   0x0E,
        '4':   0x0F,
    }
    register = {
       'communications': {'address': 0x00, 'byte': 1},
       'status':         {'address': 0x00, 'byte': 1},
       'mode':           {'address': 0x08, 'byte': 2},
       'configuration':  {'address': 0x10, 'byte': 2},
       'data':           {'address': 0x18, 'byte': 3},
       'id':             {'address': 0x20, 'byte': 1},
       'io':             {'address': 0x28, 'byte': 1},
       'offset':         {'address': 0x30, 'byte': 3},
       'fullscale':      {'address': 0x38, 'byte': 3},
    }
    
    def __init__(self, spi):
        self.spi = spi

    def reset(self):
        cmd = [0xFF, 0xFF, 0xFF, 0xFF]
        self.spi.xfer2(cmd)
    
    def read(self, cmd):
        return self.spi.xfer2(cmd)[1:]

    def write(self, cmd):
        self.spi.xfer2(cmd)

    def read_bytes(self, reg):
        cmd = [reg['address'] | 0x40] + [0x00] * reg['byte']
        return self.read(cmd)

    def write_bytes(self, reg, dat):
        cmd = [reg['address']] + dat
        self.write(cmd)

    def read_data(self, reg):
        cmd = [reg['address'] | 0x40] + [0x00] * reg['byte']
        dat = self.read(cmd)
        val = 0
        for i in range(reg['byte']):
            val <<= 8
            val += dat[i]
        return val
        
    def write_data(self, reg, val):
        cmd = [reg['address']] + [0x00] * reg['byte']
        for i in range(reg['byte'], 0, -1):
            cmd[i] = val & 0xFF
            val >>= 8
        self.write(cmd)

