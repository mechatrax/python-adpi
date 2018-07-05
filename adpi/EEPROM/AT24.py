class AT24C256():
    def __init__(self, i2c, chipaddr):
        self.i2c = i2c
        self.address = chipaddr

    def seek(self, regaddr):
        highaddr = (regaddr >> 8) & 0xFF
        lowaddr = regaddr & 0xFF
        self.i2c.write_byte_data(self.address, highaddr, lowaddr)

    def read(self, regaddr, size=32):
        self.seek(regaddr)
        dat = []
        for i in range(size):
            dat.append(self.i2c.read_byte(self.address))
        return dat

    def write(self, regaddr, dat):
        highaddr = (regaddr >> 8) & 0xFF
        lowaddr = regaddr & 0xFF
        self.i2c.write_i2c_block_data(self.address, highaddr, [lowaddr] + dat)

