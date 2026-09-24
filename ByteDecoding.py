
LoraTestString = [0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x4C, 0x6F, 0x52, 0x61, 0x21]


def GetBytes(startByte:int , endByte: int, byteArray: bytes):
    returnArry = []
    for i in range(startByte, endByte):
        returnArry.append(byteArray[i])
    return returnArry


def ByteTransform(byteArray: bytes):
    returnArray = []

    
    return bytes(byteArray).decode('ascii')


if __name__ == "__main__":
    print(ByteTransform(LoraTestString))
    print(ByteTransform(GetBytes(0,3,LoraTestString)))
    print(ByteTransform(GetBytes(5,8,LoraTestString)))
    