# -*- coding: utf-8 -*-
# Description: example netdata python.d module
# Author: Panagiotis Papaioannou (papajohn-uop)
# SPDX-License-Identifier: GPL-3.0-or-later


from bases.FrameworkServices.SimpleService import SimpleService


#those two imports are required to connect thous websockets
import websocket
from websocket import create_connection

#we tranform the result into json for easier manipulation
import json
#debug
from pprint import pprint
import random
	

NETDATA_UPDATE_EVERY=1
priority = 90000


ORDER = [
    'temp_current',
    'humid_current'
]

CHARTS = {
    'temp_current': {
         'options': ['my_temp', 'Temperature', 'Celsius', 'TEMP', 'weather_station', 'line'],
        'lines': [
            ['current_temperature']
        ]
     },
    'humid_current': {
         'options': ['my_humid', 'Humidity', '%', 'HUMIDITY', 'weather_station', 'line'],
        'lines': [
            ['current_humidity']
        ]
     }
}

class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        SimpleService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        #values to show at graphs
        self.values=dict()

	
    @staticmethod
    def check():
        return True

    weather_data=dict()
    weather_metrics=[
		  "temp","av_temp","min_temp","max_temp", 
		  "humid","av_humid","min_humid","max_humid", 
		  "pressure","av_pressure","min_pressure","max_pressure", 
		  ]
    
    def logMe(self,msg):
        self.debug(msg)
	

    def populate_data(self):
        for metric in self.weather_metrics:
            self.weather_data[metric]=random.randint(0,100)
   

    def get_data(self):
        #The data dict is basically all the values to be represented
        # The entries are in the format: { "dimension": value}
        #And each "dimension" shoudl belong to a chart.
        data = dict()
        
        self.populate_data()
        
        
        data['current_temperature'] = self.weather_data["temp"]
        data['current_humidity'] = self.weather_data["humid"]
            
        return data
