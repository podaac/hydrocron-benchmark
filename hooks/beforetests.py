from locust import events

from utils import SetupCalls
from utils.enum import Environment
from config.configManager import ConfigManager


class BeforeHooks():
        
    @events.init_command_line_parser.add_listener
    def AddCommandLineArguments(parser):
        parser.add_argument("--env", choices=["ops", "uat", "sit", "prod"], default="uat", help="Environment")
        
    
    @events.init.add_listener
    def OnStartUp(environment, **kwargs):
        print(f"Environment: {environment.parsed_options.env}")
        SetupCalls.SetUpLogging()
        ConfigManager.InitializeConfig(
            env = Environment.from_str(environment.parsed_options.env))
        print("========================================= Finished start up preparation =========================================")
        
    
    @events.test_start.add_listener
    def BeforeExecution(environment, **kwargs):
        print("========================================= Finished pre execution preparation =========================================")