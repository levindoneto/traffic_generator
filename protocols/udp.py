def getSizeBufferBytes():
    """
    Get defined size buffer in Bytes
    @param: void\n
    @returns: Int
    """
    return 1250

def getSizeBufferBits():
    """
    Get defined size buffer in bits
    @param: void\n
    @returns: Int
    """
    return getSizeBufferBytes()*8

def sendData(ip, port, bandwidth):
    """
    Send data in UDP
    @param: str, int, float\n
    @returns: void
    """
    import socket
    import time

    timeToSend = getSizeBufferBytes() * 1000/ bandwidth

    # Create UDP socket - IPv4
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Start sending data over UDP...")
    while (True):
        clientSock.sendto("dataToSend".encode(), (ip, port))
        time.sleep(timeToSend/1000000.0)

    print(timeToSend)