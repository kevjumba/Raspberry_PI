import I2C_Write
import I2C_Read
import sys
import time

def exec_cmd(input_string):
    """
    syntax:
        program A0,0x5A=3231   write to page A0, address 0x5A for hex string 3231
                                 ?CC will be uphex_addrted as well
        program A2,0x00?128      read page A2,address 0x00 for 128 bytes
    """
    hex_addr={'A0':0x50,'A2':0x51,'B0':0x58,'B2':0x59}
    return_str = ""
    read_back = 0
    compare_rw = 0
    read_before_write = 0
    if("," not in input_string):
        split_1 = ['A0', input_string]
    else:
        split_1=input_string.split(',',1)
        
    if '=' in split_1[1]: #writing mode
        split_2=split_1[1].split('=')
        register=int(split_2[0],16)
        register_str = str(register)
        
        #print split_2[2]
        if '?' in split_2[1]: 
            split_3 = split_2[1].split('?')
            if split_3[0] == '': # ? in front
                read_before_write = 1
                #if '!' in split_3[1]:
                  #  print 'bang is in'
                   # write_string = '0'
                if len(split_3)>2: #question mark in the back and front ?__?
                    read_back = 1
                    write_string = split_3[1]
                    
                    if('!' in split_3[2]): #! in the back  ?__?!
                        compare_rw = 1
                else: #question mark not in the back ?__!
                    write_string = split_3[1]
            elif len(split_3)>1: #question mark in the back but not front  __?
                write_string = split_3[0]
                read_back = 1
                if('!' in split_3[1]): #___?!
                    compare_rw = 1
        else:
            write_string = split_2[1]

        block = []
        try:
           block=write_string.decode('hex')  #see if this is ascii
           block=write_string
        except:# if it is ascii
           block=write_string.encode('hex')
#=======================================================================
        
        write = 1
        addr = hex_addr[split_1[0]]
        if(read_before_write):
            data = I2C_Read.read_block(addr, register_str, len(block)/2)
            return_str = format_block(data)
            if(return_str == block):
                write = 0 #don't write
                return_str = "Already written"
        if(write):
            I2C_Write.write_block(addr, register_str, block)
            time.sleep(0.05)
            if read_back:
                block = I2C_Read.read_block(addr, register_str, len(block)/2)
                return_str = format_block(block)
            if(compare_rw):
                return_str += "\nread and write are same" \
                if (write_string == return_str)  else "\nread and write not same"
        
                
#=======================================================================

    elif '?' in split_1[1]:
        split_2=split_1[1].split('?')
        if split_2[-1]=='':
            split_2[-1]='1'
        length = int(split_2[-1])
        register=int(split_2[0],16)
        register_str = str(register)
        block = I2C_Read.read_block(hex_addr[split_1[0]], register_str, length)
        if '??' in split_1[1]:
            return_str = format_block(block)
        else:
            block = ['{0:02X}'.format(int(i)) for i in block]
            hex_str = ','.join(block)
            hex_block = [x.decode('hex') for x in block]
            ascii_list = [x if ord(x) in range (32, 126) else ' ' for x in hex_block]
            ascii_str = ''.join(ascii_list)
            return_str = hex_str + ' => '+ascii_str
    return(return_str)
    
def format_block(block):
    block = ['{0:02X}'.format(int(i)) for i in block]
    return_str = ''.join(block)
    return return_str
if(__name__ == "__main__"):
    print(exec_cmd(sys.argv[1]))
