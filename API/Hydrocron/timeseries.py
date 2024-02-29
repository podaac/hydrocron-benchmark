from utils.enum import TimeseriesFeature, TimeseriesOutput

import requests
import datetime

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "timeseries"

class Timeseries():
    
    def __init__(self):
        self.session = requests.session()
    
    
    def Ping(self,
            feature:TimeseriesFeature = TimeseriesFeature.Reach,
            output:TimeseriesOutput = TimeseriesOutput.geojson,
            startdate:datetime = None,
            enddate:datetime = None,
            fields:list = [],
            logging:bool = True) -> requests.Response:
        
        if logging:
            print(f'\r\nGetting a Ping...')
            
        # Test featrure Id
        featureId = "00001100011"
        fullurl = f'{globalVars.HYDROCRON_baseurl}/{endpoint}?feature={feature.name}&feature_id={featureId}&output={output.name}'
        
        if startdate != None:
            fullurl += f'&start_time={startdate.isoformat(timespec="seconds")}'
        if enddate != None:
            fullurl += f'&end_time={enddate.isoformat(timespec="seconds")}'
        if fields != []:
            fieldsText = ""
            for field in fields:
                fieldsText += f'{field},'
            fieldsText = fieldsText[:-1]
            fullurl += f'&fields={fieldsText}'
        
        custom_header = {
            "Content-Type": "application/json" }
        
        print(f'fullurl: {fullurl}')
        response = self.session.post(
            url = fullurl,
            headers = custom_header)
        
        if logging:
            print(f"Response: {response.status_code}")
            if response.status_code != 200:
                print(f"Response text:\r\n{response.text}\r\n")
                print(f"Request url:\r\n{response.request.url}\r\n")
                print(f"Request body:\r\n{response.request.body}\r\n")
        return response