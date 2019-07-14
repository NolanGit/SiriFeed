import sys
import time
import platform
import configparser

from weather_getter import Weather

location = sys.argv[0]


def get_key():
    cf = configparser.ConfigParser()
    if 'Windows' in platform.platform() and 'Linux' not in platform.platform():
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' Using C:/Users/sunhaoran/Documents/GitHub/ServerTools/ServerTools.config ...')
        cf.read('C:/Users/sunhaoran/Documents/GitHub/ServerTools/ServerTools.config')
    elif 'Linux' in platform.platform() and 'Ubuntu' not in platform.platform():
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' Using /home/pi/Documents/Github/ServerTools/RaspberryPi.config ...')
        cf.read('/home/pi/Documents/Github/RaspberryPi.config')
    elif 'Ubuntu' in platform.platform():
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' Using /root/Documents/GitHub/ServerTools/ServerTools.config ...')
        cf.read('/root/Documents/GitHub/ServerTools/ServerTools.config')
    key = (cf.get('config', 'KEY'))
    return key


key = get_key()
weather = Weather()

today_tmp_max, today_tmp_min = weather.get_temp(key, 'changchun')

aqi_json = weather.get_aqi(key, 'changchun')
city_aqi = aqi_json['air_now_city']
print(today_tmp_max, today_tmp_min, city_aqi)
