from utils.enum import Environment
from utils.filehandler import FileHandler

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

class ConfigManager():

    def InitializeConfig(
        env:Environment,
        threadCount:int=0):
        
        print(f"\r\nSetting config file variables...")

        envVariableJson = FileHandler.GetJsonFileContent("env.json", "./config")

        # Global
        if type(env) != Environment:
            globalVars.Environment = Environment.from_str(str(env))
        else:
            globalVars.Environment = env

        # Parallel execution / threading
        globalVars.Threading_Enable = threadCount > 1
        globalVars.Threading_Execution_Count = threadCount
    
        # Hydrocron
        globalVars.SOTO_baseurl = envVariableJson[env.name]['SOTO_API_BASEURL']
