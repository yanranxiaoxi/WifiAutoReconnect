#!/usr/bin/python
import os, sys

params = sys.argv

if 'full' not in os.popen('sudo nmcli networking connectivity').read():
    print('\nWARNING: Wi-Fi is down, restarting...\n')
    os.system('sudo nmcli connection up "' + params[1] + '"')
else:
    print('\nINFO: Wi-Fi is currently working.\n')
