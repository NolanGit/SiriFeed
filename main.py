import sys
import time
import platform
import configparser

from weather_getter import Weather

location = sys.argv[1]
MORNING_TIME = 1000
AM = 1130
PM = 1400
NIGHTTIME1 = 1730
NIGHTTIME2 = 500


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


#问候
current_time = int(time.strftime("%H:%M", time.localtime()))
greetings=''
if (NIGHTTIME2 < current_time < MORNING_TIME): greetings = '早上好。'
if (MORNING_TIME < current_time < AM): greetings = '上午好。'
if (AM < current_time < PM): greetings = '中午好。'
if (PM < current_time < NIGHTTIME1): greetings = '下午好。'
if ((000 < current_time < NIGHTTIME2) or (NIGHTTIME1 < current_time < 2400)): greetings = '晚上好。'

#天气
key = get_key()
weather = Weather()
today_tmp_max, today_tmp_min = weather.get_temp(key, location)
aqi_json = weather.get_aqi(key, location)
city_air = aqi_json['air_now_city']
city_air_condition = city_air['qlty']
city_aqi = city_air['aqi']
comfort, clothes = weather.get_lifestyle(key, location)
weather_content = '你现在在' + location + '，最高气温' + str(today_tmp_max) + '度，' + '最低气温' + str(today_tmp_min) + '度，' + '空气质量' + str(city_air_condition) + '，AQI' + str(
    city_aqi) + '。' + comfort + clothes + '最高气温' + str(today_tmp_max) + '度，' + '最低气温' + str(today_tmp_min) + '度。'

print(greetings + weather_content)
