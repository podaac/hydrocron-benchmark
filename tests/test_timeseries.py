from locust import HttpUser, task, tag, events
from requests import Response


from API.Hydrocron import Timeseries

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

@tag('timeseries')
class TestTimeseries(HttpUser):

# ========================================== Timeseries ==========================================
    @tag('positive')
    @task
    def test_Timeseries_200(self):
        expectedStatusCode = 200
        client_Timeseries = Timeseries()
        client_Timeseries.session = self.client
        response:Response = client_Timeseries.Ping()
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        