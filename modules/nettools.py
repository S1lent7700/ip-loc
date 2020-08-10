import os, sys, socket, re, time
from socket import *
from modules.meta.colors import Normal as n, Bold as b
from modules.meta._meta import Settings, Lists

# Set the default system encoding
sys.getdefaultencoding()
# -*- coding: UTF-8 -*-

"""
Networking Utilities: Port Scanning (basic/intermediate/advanced), "Alive" testing, etc
"""

class NetTools:

    def __init__(self, ip_address, port=443, ports=None):
        self.host = ip_address
        self.port = port
        if ports is None:
            self.ports = []
        else:
            self.ports = ports

    def simple_port_scan_open(self):    # Complete
        setp = Settings()
        listp = Lists()
        t = time.time()

        try:
            # Print scan start banner
            try:
                print("\n" + b.ysb + "=>> Starting scan on IP (50-2,000): " + b.gsb + self.host + b.ysb + " - Time: " +
                      b.gsb,time.time(),b.ceb + "\n")
            except KeyboardInterrupt:
                print("\n" + n.ws + "Ctrl + C Caught, exiting..." + n.ce + "\n"); exit(0)
            # Scan the host using the port array found in the Lists section of '_meta'
            for i in range(50, 2000):
                try:
                    sock = socket(AF_INET, SOCK_STREAM)
                    sock.settimeout(2)
                    # Connect value
                    connect = sock.connect_ex((self.host, int(i)))
                    #
                    if connect == 0:
                        # Print the open port.
                        print(n.ws + "++ " + n.ys + "Open port on (" + n.gs + self.host + n.ys + ") - Port: " + n.gs,int(i),n.ce)
                        listp.simple_ports.append(int(i))
                    else:
                        print(n.bs + "** " + n.ws + "Waiting on [" + n.ys + self.host + ":",int(i),n.ws + "] ... " + n.ce)
                    # Close the active socket after iteration loop is done
                    sock.close()
                except Exception as e:
                    print("\n" + n.rs + "[Error][1] " + n.ws + "-> " + str(e) + n.ce + "\n"); exit(1)
                # Catch the keyboard interrupt
                except KeyboardInterrupt:
                    print("\n" + n.ws + "Ctrl + C Caught, exiting..." + n.ce + "\n"); exit(0)
            # After the port scan is complete, print out the ending result message
            print("\n" + b.wsb + "Scan Complete -- Time: ", b.ysb, (time.time() - t), b.wsb + " -- Ports Scanned: " +
                  b.ysb, len(listp.simple_ports), b.ceb + "\n")
        except Exception as e:
            print("\n" + n.rs + "[Error][2] " + n.ws + "-> " + str(e) + n.ce + "\n"); exit(1)

    def nmap_port_scan(self):
        pass