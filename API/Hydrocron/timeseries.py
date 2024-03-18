from utils.enum import TimeseriesFeature, TimeseriesOutput

import requests
import datetime

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "hydrocron/v1/timeseries"

class Timeseries():
    
    def __init__(self):
        self.session = requests.session()
    
    
    def GetTimeseries(self,
            startdate:datetime = None,
            enddate:datetime = None,
            feature:TimeseriesFeature = TimeseriesFeature.Reach,
            output:TimeseriesOutput = TimeseriesOutput.geojson,
            fields:list = ['reach_id', 'time_str', 'wse', 'geometry'],
            logging:bool = True) -> requests.Response:
        
        if logging:
            print(f'\r\n========================= Getting a Timeseries... =========================')
            
        # Test featrure Id
        featureId = "00001100011"
        fullurl = f'{globalVars.SOTO_baseurl}/{endpoint}?feature={feature.name}&feature_id={featureId}&output={output.name}'
        
        if startdate == None:
            startdate = datetime.datetime(2020, 1, 1)
        if enddate == None:
            enddate = datetime.datetime.now()
            # Set to the start of day so there are no instance for each seconds in the report
            enddate = enddate.replace(hour=0, minute=0, second=0) 
        fullurl += f'&start_time={startdate.isoformat(timespec="seconds")}Z'
        fullurl += f'&end_time={enddate.isoformat(timespec="seconds")}Z'
        fieldsText = ""
        for field in fields:
            fieldsText += f'{field},'
        fieldsText = fieldsText[:-1]  # Remove the tailing ','
        fullurl += f'&fields={fieldsText}'
        custom_header = {
            "Host": f'{globalVars.SOTO_baseurl[8:]}' }
            # "Host": f'127.0.0.1:8888' }
        
        response = self.session.get(
            url = fullurl,
            headers = custom_header,
            allow_redirects = True)
        
        if logging:
            print(f"Response: {response.status_code}")
            if response.status_code != 200:
                print(f"Response text:\r\n{response.text}\r\n")
                print(f"Request url:\r\n{response.request.url}\r\n")
                print(f"Request headers:\r\n{response.request.headers}\r\n")
                print(f"Request body:\r\n{response.request.body}\r\n")
        return response
    