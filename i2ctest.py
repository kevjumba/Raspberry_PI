from smbus2 import SMBusWrapper
import sys
import math
i2c_addr = 0x50
offset = 0x54
i2c_auth_addr = 0x51
auth_offset =0x7B

password = [0x12, 0x34, 0x56, 0x78]
block = []
with SMBusWrapper(1) as bus:
        print("writing to i2c...")
        bus.write_i2c_block_data(i2c_auth_addr, auth_offset, password)
        #print('{0:2X}'.format(bus.read_byte_data(i2c_addr, write_offset)))
        byte_string = sys.argv[2]
        block = [int(byte_string[i:i+2]) for i in range(0, len(byte_string), 2)]
        register_num = int(sys.argv[1])
        print(register_num)
	start = int(sys.argv[1], 16) #decimal form of starting registry
        nearest_register = math.ceil(start/8.0)*8
        first_write_len = int(nearest_register - start)
	"""write first bytes"""
        print("writing block ")
	print(block[0:first_write_len])
	bus.write_i2c_block_data(i2c_addr, register_num, block[0:first_write_len])
	index = 0
	while len(block)-first_write_len-index*8>8:
            temp_register = start + first_write_len + index*8
	    bus.write_i2c_block_data(i2c_addr, temp_register, block[first_write_len+index*8, first_write_len + index*8+8]
            print("writing block ")
	    print(block[first_write_len+index*8: first_write_len + index+8 + 8])
	    index = index+1
	last_write_len = len(block)-first_write_len - index*8
	last_register = start + first_write_len + index*8
	bus.write_i2c_block_data(i2c_addr, last_register, block[first_write_len + index*8, first_write_len + index*8 + last_write_len]
	print("writing block ")
	print(block[first_write_len + index*8: first_write_len + index*8 + last_write_len])
        #bus.write_i2c_block_data(i2c_addr, int(sys.argv[1]), block)
        #bus.write_byte_data(i2c_addr, int(sys.argv[1]), int(sys.argv[2]))
        #print('{0:2X}'.format(bus.read_byte_data(i2c_addr, offset)))
	#print(bus.read_i2c_block_data(i2c_addr, int(sys.argv[1]), int(sys.argv[2])))
	#data = bus.read_i2c_block_data(i2c_addr, offset, 6)
	#for i in data:
	#	print '{0:2X}'.format(i), 
