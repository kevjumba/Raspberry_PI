from smbus2 import SMBusWrapper
import sys
i2c_addr = 0x50
i2c_auth_addr = 0x51
auth_offset =0x7B

password = [0x12, 0x34, 0x56, 0x78]
block = [0x32, 0x36, 0x31, 0x33, 0x35, 0x38]
def read_block(addr, registry, length):

    register = int(registry) #decimal form of starting registry
    with SMBusWrapper(1) as bus:
        data = []
        index = 0
        if length>32:
            while length > 32:
                data = data + bus.read_i2c_block_data(addr, register+32*index, 32)
                length = length-32
                index+=1
        data= data + bus.read_i2c_block_data(addr, register+32*index, length)
        return data


if(__name__ == '__main__'):
	data = read_block(i2c_addr, int(sys.argv[1]), int(sys.argv[2]))
        hex_list = ['{0:02X}'.format(x) for x in data]
        hex_str = ''.join(hex_list)
        print(hex_str)


