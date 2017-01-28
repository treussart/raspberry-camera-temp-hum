# raspberry-camera-temp-hum
Send Temperature and Humidity of AM2302 sensor to Domoticz

Use a Raspberry Pi with a camera module and a am2302 sensor 

Requirements
-------------
* [Python3][1].
* [Domoticz][2].
* [Am2302 sensor][3].
* [Camera module][4].

Installation
-------------

Create a Virtual Sensors in Domoticz :
* a subType Temp + Humidity.

Edit the cron, example :

    crontab -e
Add :

    0 * * * * python ~/raspberry-camera-temp-hum/cron/sendTempHumToDomoticz.py

[1]: https://www.python.org/downloads/
[2]: https://github.com/domoticz/domoticz
[3]: https://www.adafruit.com/product/393
[4]: https://www.adafruit.com/products/3099
