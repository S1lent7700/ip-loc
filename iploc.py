from argparse import ArgumentParser
from modules.meta._meta import Settings
from modules.stringutil import StringUtil
from modules.nettools import NetTools

"""
This (module) program takes an IP address and basically does a "probe" lookup.
This program can look up the packet, data, and website information as well as
retrieve the country the IP address resides in. Python Version: 3.8. Connections
to sites can be tested through this program as well.
"""

## Initialize classes
setp = Settings()
all_info = StringUtil()

## Main driver method
def main():
    # Initialize the argument parser and set globals
    global setp
    global all_info

    parse = ArgumentParser(usage="iploc.py -I <IP_ADDRESS_OF_WEBSITE> [OPTIONS] | -h, --help", conflict_handler="resolve")
    # Default group 1
    gp1 = parse.add_argument_group("Group 1: Default Group", "Basic default functions")
    gp1.add_argument('-I', '--ip', default=None, type=str, dest="iploc_ip", metavar="", help="Set the IP address to probe.")
    gp1.add_argument('-V', '--version', action="store_true", dest="iploc_ver", help="Print program version and exit.")
    gp1.add_argument('--all-info', action="store_true", dest="iploc_all_info", help="Print all basic program info...")
    gp1.add_argument('--set-host', type=str, dest="iploc_set_ip", default=None, metavar="", help="Set the IP address so that you don't have to use"
                                                                                   " the [-I/--ip] option...")
    gp1.add_argument('--set-hosts', type=str, dest="iploc_set_hosts", metavar="", help="Set an array of hosts -- Host strings must be"
                                                                                       " separated by a comma.")

    gp2 = parse.add_argument_group("Group 2: IP Location Group", "Get IP (Server/Service) Location")
    gp2.add_argument('-S', '--state', action="store_true", dest="iploc_get_srv_state", help="Get the state the server is located in.")
    gp2.add_argument('-C', '--country', action="store_true", dest="iploc_get_srv_country", help="Get the country the server is located in.")

    gp3 = parse.add_argument_group("Group 3: Network Group", "Get [network] details in IP address/Host")
    gp3.add_argument('--port-scan:[simple, single, multi, simple-multi]', type=str, dest="iploc_port_scan", metavar="",
                     help="Scan one or more ports using the following modes '[]'")
    gp3.add_argument('--use-nmap', type=str, dest="iploc_useNamp", metavar="", help="Use Nmap to scan port(s) -- Extra Args required.")

    # Local objects

    # Query the arguments thus fully initializing the parser
    args = parse.parse_args()
    # *********************************************************************************************************
    # Basic Group Functions
    if args.iploc_ver:
        setp = Settings()
        print("Program Version: " + setp.version); exit(0)

    if args.iploc_all_info:
        print("\n")
        all_info.print_all_info(); print("\n"); exit(0)

    if args.iploc_set_ip:
        if args.iploc_set_ip is None:
            return
        else:
            setp.ip_address = args.iploc_set_ip; exit(0)
    # *********************************************************************************************************
    # IP Location

    # *********************************************************************************************************
    # Networking
    if args.iploc_port_scan:
        net = NetTools(args.iploc_ip)

        # Split the port scan argument using the ':' character
        # We will need everything AFTER the ':' character so [1:]
        arg_ps = str(args.iploc_port_scan).split(':')
        # Check to see what argument is given for the port scan (multi, default, etc)
        if args.iploc_port_scan == "simple":
            # Run the simple port scan
            net.simple_port_scan_open()

    # *********************************************************************************************************

if __name__ == '__main__':
    main()
