#!/usr/bin/python
# coding: utf8
import pycurl
import Adafruit_DHT
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Host of Domoticz", default='192.168.0.8')
parser.add_argument("--port", help="Port of Domoticz", default='8080')
parser.add_argument("--idx", help="Device number of Domoticz", default='81')
parser.add_argument("--sensor", help="Type of sensor", default='2302')
parser.add_argument("--pin", help="pin number of GPIO", default='4')
args = parser.parse_args()

host = args.host
port = args.port
idx = args.idx
sensor = args.sensor
pin = args.pin


def getTempHum(sensor, pin):
    sensor_args = {'11': Adafruit_DHT.DHT11,
                   '22': Adafruit_DHT.DHT22,
                   '2302': Adafruit_DHT.AM2302}
    sensor = sensor_args[sensor]
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


def sendToDomoticz(host, port, idx, temperature, humidity):
    if humidity is not None and temperature is not None:
        c = pycurl.Curl()
        url = 'http://' + str(host) + ':' + str(port) + '/json.htm?type=command&param=udevice&idx=' + str(idx) + '&nvalue=0&svalue='\
        + str("{0:.2f}".format(temperature)) + ';' + str("{0:.2f}".format(humidity)) + ';0'
        c.setopt(c.URL, url)
        c.perform()
        c.close()
        sys.exit(0)
    else:
        print('Failed to send to domoticz. Try again!')
        sys.exit(1)


humidity, temperature = getTempHum(sensor, pin)
sendToDomoticz(host, port, idx, temperature, humidity)
sys.exit(0)
