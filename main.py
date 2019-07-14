import sys
import time
import platform
import configparser

from weather_getter import Weather

location = sys.argv[0]


def get_key():
    cf = configparser.ConfigParser()
    if 'Windows' in platform.platform() and 'Linux' not in platform.platform():
        cf.read('C:/Users/sunhaoran/Documents/GitHub/ServerTools/ServerTools.config')
    elif 'Linux' in platform.platform() and 'Ubuntu' not in platform.platform():
        cf.read('/home/pi/Documents/Github/RaspberryPi.config')
    elif 'Ubuntu' in platform.platform():
        cf.read('/root/Documents/GitHub/ServerTools/ServerTools.config')
    key = (cf.get('config', 'KEY'))
    return key


key = get_key()
weather = Weather()

today_tmp_max, today_tmp_min = weather.get_temp(key, 'changchun')

aqi_json = weather.get_aqi(key, 'changchun')
city_aqi = aqi_json['air_now_city']
city_air_condition = aqi_json['qlty']
print('你现在在'+location+'，最高气温'+str(today_tmp_max)+'度，'+'最低气温'str(today_tmp_min)+'度，'+'空气质量'+ str(city_air_condition)+'AQI'+str(city_aqi))
