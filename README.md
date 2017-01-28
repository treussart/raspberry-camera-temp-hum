# raspberry-camera-temp-hum
Send Temperature and Humidity of AM2302 sensor to Domoticz

Use a Raspberry Pi with a camera module and a am2302 sensor 

Requirements
-------------
* [Python3][1].
* [Domoticz][2].
* [Am2302 sensor][3].
* [Raspberry Pi][5].
* [Raspberry Pi Camera module][4].
* [Raspberry Pi Camera Box Bundle][6].
* (Optional)[Breadboarding wire][7].

Installation
-------------

**Domoticz**

Create a Virtual Sensors in Domoticz :
* a subType Temp + Humidity.


**Raspberry Pi**

Install Adafruit Python Library :

    sudo apt install rpi.gpio git build-essential python-dev   
    cd ~/
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git  
    cd Adafruit_Python_DHT 
    sudo python setup.py install 

Install Motion :

    sudo apt-get install motion libav-tools
    sudo modprobe bcm2835-v4l2
    sudo echo 'sudo modprobe bcm2835-v4l2' >> /etc/rc.local  
    sudo touch /tmp/motion.log
    sudo chmod 775 /tmp/motion.log

    sudo nano /etc/motion/motion.conf
    
> - Log ~/camera/motion.log
> -  width 1080
> - height 576
> - framerate 15
> - threshold 4000
> - lightswitch 100
> - minimum_motion_frames 1
> - output_pictures off
> - ffmpeg_output_movies on
> - ffmpeg_video_codec mpeg4
> - target_dir ~/camera
> - stream_port 8081
> - stream_localhost off
> - #sdl_threadnr 0
> - movie_filename %Y%m%d%H%M%S-%v

(Optional - Problem with the change in brightness due to clouds)
> - on_movie_start python3 ~/raspberry-camera-temp-hum/motionCamera.py

Edit the cron, example :

    crontab -e
Add :

    0 * * * * python3 ~/raspberry-camera-temp-hum/cron/sendTempHumToDomoticz.py
    0 0 * * 0 sh ~/raspberry-camera-temp-hum/cron/eraseCameraFiles.sh 

[1]: https://www.python.org/downloads/
[2]: https://github.com/domoticz/domoticz
[3]: https://www.adafruit.com/product/393
[4]: https://www.adafruit.com/products/3099
[5]: https://www.adafruit.com/products/3055
[6]: https://www.modmypi.com/raspberry-pi/cases/modmypi-camera-boxes/nwazet-pi-camera-box-bundle-case,-lens-and-wall-mount-b-plus
[7]: https://www.adafruit.com/products/153
