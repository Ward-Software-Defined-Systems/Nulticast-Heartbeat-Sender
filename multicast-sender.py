#!/usr/bin/python3

import time
import socket
import sys
import secrets
import string
import signal


def handler(signum, frame):
    print('\nSIGNUM: ' + str(signum) + '\n' + 'FRAME: ' + str(frame) + '\n')
    res = input("Ctrl-c was pressed. Do you want to exit? y/n ")
    if res == 'y':
        exit(1)


signal.signal(signal.SIGINT, handler)


def help_and_exit(prog):
    print('Usage: ./multicast-sender.py [MCAST GROUP] [PORT] [TTL]')
    print('Usage: ./multicast-sender.py 239.0.1.2 5004 3')
    sys.exit(1)


def mc_send(mcgrpip, mcport, ttl):
    # This function is a modified pattern commonly found on the Internet.
    # Referenced and repurposed.

    # Alphabet used to generate heartbeat message
    s_alphabet = string.ascii_letters + string.digits + string.punctuation

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,ttl)

    # Generate and send messages/heartbeats
    while(True):
        heartbeat = ''.join(secrets.choice(s_alphabet) for i in range(24))
        sock.sendto(bytes(heartbeat, 'utf-8'), (mcgrpip, mcport))
        print ("SENT MULTICAST HEARTBEAT --> " + mcgrpip + ":" + str(mcport) + ": " + heartbeat)
        time.sleep(1)


def main(argv):
    if len(argv) < 4:
        help_and_exit(argv[0])

    # Input validation can be added prior to assigning vars or passing prams:
    mcgrpip = argv[1]
    mcport = int(argv[2])
    ttl = int(argv[3])

    mc_send(mcgrpip, mcport, ttl)


if __name__=='__main__':
     main(sys.argv)
