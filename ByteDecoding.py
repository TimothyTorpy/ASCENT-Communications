
LoraTestString = [0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x4C, 0x6F, 0x52, 0x61, 0x21]


# def ByteDecode(startByte: int, endByte: int , byteArray: bytes):
#     byteStart = startByte * 4


def ByteTransform(byteArray: bytes):
    returnArray = []

    
    return bytes(byteArray).decode('ascii')


if __name__ == "__main__":
    print(ByteTransform(LoraTestString))
    