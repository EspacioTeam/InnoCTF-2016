def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))


data = bytearray(open('flag.png', 'rb').read())
key = bytearray([0x,0x,0x,0x,0x])
output = xor(data, key)
open('flag.png.bin', 'wb+').write(output)