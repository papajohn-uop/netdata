# -*- coding: utf-8 -*-
# Description: howto  python.d module
# Author: Panagiotis Papaioannou (papajohn-uop)
# SPDX-License-Identifier: GPL-3.0-or-later


from bases.FrameworkServices.SimpleService import SimpleService



import random
	

NETDATA_UPDATE_EVERY=1
priority = 90000


ORDER = [
    "demo_chart"
]

CHARTS = {
    "demo_chart": {
        'options': ["demo_name", "demo_title", "demo_units", "demo_family", "demo_context", "line"],
        "lines": [
            ["demo_line_id","demo_line_name"]
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

    
    def logMe(self,msg):
        self.debug(msg)
	


    def get_data(self):
        #The data dict is basically all the values to be represented
        # The entries are in the format: { "dimension": value}
        #And each "dimension" shoudl belong to a chart.
        data = dict()
        self.logMe("Demo plugin") 
        random_value = random.randint(0,100) 
        data["demo_line_id"] = random_value
            
        return data
