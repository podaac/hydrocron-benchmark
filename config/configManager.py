from utils.enum import Environment
from utils.filehandler import FileHandler

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

class ConfigManager():

    def InitializeConfig(
        env:Environment):
        
        print(f"\r\nSetting config file variables...")

        envVariableJson = FileHandler.GetJsonFileContent("env.json", "./config")

        # Global
        globalVars.Environment = env

        # Hydrocron
        globalVars.HYDROCRON_baseurl = envVariableJson[env.name]['HYDROCRON_API_BASEURL']
