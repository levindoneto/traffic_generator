'''
Usage:
  python gt.py –i destinationIp –p port -r bandwidth”
Options:
  - i String  The IP to send the datagram to
  - p Integer The port of the communication
  - r Float   The bandwidth the datagrams are transmitted in

UDP traffic generator
'''

import protocols.udp as udp
import shell.options as options
import sys

def main(args):
    arg = options.getArgs(args)
    if (arg != -1):
        print("UDP traffic generator: ", arg)

if __name__ == '__main__':
    main(sys.argv)