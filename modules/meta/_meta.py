"""
A meta module -- Meta strings and settings
"""
import os, sys

class Strings:
    # Begin
    sys_version = sys.version
    sys_platform = sys.platform
    sys_api_version = sys.api_version

class Settings:
    def __init__(self):
        self.program = "IP Loc"
        self.version = "1.0a"
        self.author = "S1lent"
        self.email = "hsk.2290s1@gmail.com"
        self.cwd = os.getcwd()                   # Should be the meta level
        self.default_profile = "profile.ip-loc"  # Default config profile (user)
        self.app_profile = "config.ip-loc"       # Default program configuration profile
        self.default_loHost = "127.0.0.1"        # Loop back address
        self.ip_address = ""                     # The user can set this ip address
        self.old_geo_datafile = "GeoIP.dat"      # The old GeoIP database
        self.old_geo_asn = " GeoIPASNum.dat"     # ASN number data
        self.old_geo_ipv6 = "GeoIPv6.dat"        # IPv6 data
        self.old_geo_city = "GeoLiteCity.dat"    # City data
        self.ip2loc_binary_stdrd = "IP2LOCATION-LITE-DB11.BIN"   # IP2Location standard binary


class Lists:
    def __init__(self):
        self.info_keys = ["Author", "Email", "Version", "Module"]
        self.ports = [21, 22, 23, 37, 80, 81, 443, 3306]
        self.custom_ports = []
        self.simple_ports = []
        self.hosts = []

class Dictionaries:
    def __init__(self):
        self.prog_info_dict = {"Author": "S1lent", "Email": "hsk.2290s1@gmail.com", "Version": "1.0a", "Module": "IP Loc"}
