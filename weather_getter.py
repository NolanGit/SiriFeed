# -*- coding:utf-8 -*-
import os
import sys
import time
import peewee
import datetime
import requests
class Weather(object):

    def __init__(self):
        pass

    def get_temp(self, key: str, location: str):
        payload = {'location': location, 'key': key}
        r = requests.get('https://free-api.heweather.com/s6/weather/forecast', params=payload)
        today_forecast = r.json()['HeWeather6'][0]['daily_forecast'][0]
        today_tmp_max = today_forecast['tmp_max']  # 今天最高气温
        today_tmp_min = today_forecast['tmp_min']  # 今天最低气温
        return (today_tmp_max, today_tmp_min)

    def get_aqi(self, key: str, location: str):
        payload = {'location': location, 'key': key}
        r = requests.get('https://free-api.heweather.net/s6/air/now', params=payload)
        return (r.json()['HeWeather6'][0])

    def get_lifestyle(self, key: str, location: str):
        payload = {'location': location, 'key': key}
        r = requests.get('https://api.heweather.net/s6/weather/now', params=payload)
        comfort = r.json()['HeWeather6'][0]['lifestyle'][0]['txt']
        clothes = r.json()['HeWeather6'][0]['lifestyle'][1]['txt']
        return (comfort, clothes)
