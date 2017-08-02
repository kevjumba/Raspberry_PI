from smbus2 import SMBusWrapper
import sys
i2c_addr = 0x50
offset = 0x54
i2c_auth_addr = 0x51
auth_offset =0x7B

password = [0x12, 0x34, 0x56, 0x78]
block = [0x32, 0x36, 0x31, 0x33, 0x35, 0x38]
with SMBusWrapper(1) as bus:
        print("writing to i2c...")
        bus.write_i2c_block_data(i2c_auth_addr, auth_offset, password)
        #print('{0:2X}'.format(bus.read_byte_data(i2c_addr, write_offset)))
	#bus.write_i2c_block_data(i2c_addr, offset, block)
        #bus.write_byte_data(i2c_addr, offset, 32)
        #print('{0:2X}'.format(bus.read_byte_data(i2c_addr, offset)))
	length = int(sys.argv[2])
	registry = int(sys.argv[1])
	data = []
	if length>32:
	    while length > 32:

	        data = data + bus.read_i2c_block_data(i2c_addr, registry, 32)
		length = length-32
	print("out")
	data= data +bus.read_i2c_block_data(i2c_addr, registry, length)
	for i in data:
		print '{0:2X}'.format(int(i)), 
