#!/usr/bin/python3
# coding: utf8
from urllib.parse import quote
import urllib.request
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Host of Domoticz", default='192.168.0.8')
parser.add_argument("--port", help="Port of Domoticz", default='8080')
parser.add_argument("--idx", help="Device number of Domoticz", default='81')
parser.add_argument("--message", help="Message to display", default='Motion Detected')
args = parser.parse_args()

host = args.host
port = args.port
idx = args.idx
value = args.message


def sendToDomoticz(host, port, idx, value, level):
    url = 'http://' + host + ':' + port + '/json.htm?type=command&param=udevice&idx=' + str(idx) + '&nvalue=' + \
          str(level) + '&svalue=' + quote(value.encode('utf8'))
    urllib.request.urlopen(url)


sendToDomoticz(host, port, idx, value, 4)
sys.exit(0)
