def getArgs(argsStr):
    """
    Get args from command prompt
    @param: str\n
    @returns: obj
    """
    ip = "192.168.0.1"
    port = 5050
    bandwidth = 1000.0
    return {
        "ip": ip,
        "port": port,
        "bandwidth": bandwidth
    }