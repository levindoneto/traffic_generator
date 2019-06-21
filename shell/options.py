def getArgs(argsLst):
    """
    Get args from command prompt
    @param: list\n
    @returns: obj
    """
    if (argsLst[1] != "-i" and argsLst[3] != "–p" and argsLst[5] != "–r"):
        print("Invalid options given\npython gt.py –i destinationIp –p port -r bandwidth")
        return -1
    else:
        try:
            ip = str(argsLst[2])
            port = int(argsLst[4])
            bandwidth = float(argsLst[6])
        except:
            print("Invalid values given\npython gt.py –i STRING_IP –p INT_PORT -r FLOAT_BANDWIDTH")
            return -1
    return {
        "ip": ip,
        "port": port,
        "bandwidth": bandwidth
    }