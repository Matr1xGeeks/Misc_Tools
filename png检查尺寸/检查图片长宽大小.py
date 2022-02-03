import os
import binascii
import struct
misc = open("1.png","rb").read()

# 爆破宽
for i in range(1024):
	data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]  #IHDR数据
	crc32 = binascii.crc32(data) & 0xffffffff
	if crc32 == 0xC20F1FC6: #IHDR块的crc32值
		print(i)
		print("hex:"+hex(i))

# 爆破高		
for i in range(1024):
    data = misc[12:20] + struct.pack('>i',i)+ misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0xC20F1FC6:
        print(i)
        print("hex:"+hex(i))