from requests import Response

from API.Hydrocron import Timeseries

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

class TestPing:

# ========================================== generateL2RasterProduct ==========================================

    def test_Ping_200(self):
        expectedStatusCode = 200
        response:Response = Timeseries.Ping()
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        