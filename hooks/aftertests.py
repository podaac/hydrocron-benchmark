from locust import events


class AfterHooks():
    
    @events.quitting.add_listener
    def OnShutDown(environment, **kwargs):
        print("========================================= Finished shut down cleanup =========================================")

    
    @events.test_stopping.add_listener
    def AfterExecution(environment, **kwargs):
        print("========================================= Finished post execution cleanup =========================================")
