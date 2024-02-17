import argparse
import pytest
import threading

from time import sleep
from config.configManager import ConfigManager
from utils.enum import Environment
from utils import SetupCalls

import config.globalvariables


# File wide variables
globalvars = config.globalvariables.GlobalVariables

def _ParseArgs():
    """
    Parses the program arguments
    Returns
    -------
    args
    """

    parser = argparse.ArgumentParser(
        description='Input arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-e', '--env',
                        help='Environment used to check API of.',
                        required=True,
                        choices=["uat", "UAT", "ops", "OPS", "sit", "SIT", "ngap_uat", "ngap_ops", "ngap_sit"],
                        metavar='ops, uat, sit')
    parser.add_argument('-t', '--thread-count',
                        help='How many thread to execute the tests simultaniously',
                        required=False,
                        type=int,
                        default=1)
   
    args = parser.parse_args()
    return args

def _Run():
    """
    Run from command line.

    Returns
    -------
    """

    _args = _ParseArgs()
    environment = Environment.from_str(_args.env)
    threadCount = _args.thread_count

    SetupCalls.SetUpLogging()
    ConfigManager.InitializeConfig(
        env = environment,
        threadCount = threadCount)
    argumentList = ["tests", "--junitxml=./test-results/report.xml", '-v']
    # pytest.main(argumentList)
    
    # Set up paralel execution
    threads = []
    threading.excepthook = _CustomHooks
    for i in range(globalvars.Threading_Execution_Count):
        print(f'\r\n======================== Creating thread #{i} ========================')
        # iteratedStepList = stepList.replace('<LoadTestIterator>', f'{i}')
        print(f'Thread name set to: "{i}"')
        # print(f'Thread "{i}" step list:\r\n{iteratedStepList}')
        proc = threading.Thread(target = pytest.main(argumentList))
        proc.setName(i)
        proc.start()
        threads.append(proc)
    
    for proc in threads:
        proc.join()

    timeoutCount = 30
    aliveCount = len(threads)
    while aliveCount > 1 and timeoutCount > 0:
        aliveCount = len(threading.enumerate())
        if aliveCount > 1:
            sleep(1)
            timeoutCount -= 1
    
def _ExecuteTests(argumentList:list):
    try:
        pytest.main(argumentList)
    except AssertionError as e:
        raise e
    
def _CustomHooks(args):
    currentThread = threading.currentThread().getName()
    if currentThread.lower() != 'mainthread':
        if 'Thread_Info' not in globalvars.TempStorageDict.keys():
            globalvars.TempStorageDict['Thread_Info'] = {}
        exceptionName = args.exc_type.__name__
        message = args.exc_value
        if 'traceback' in message.args[0].lower():
            tracebackIndex = message.args[0].lower().index('traceback')
            exceptionInfo = (exceptionName, message.args[0][:tracebackIndex])
        else:
            exceptionInfo = (exceptionName, message.args[0])
        globalvars.TempStorageDict['Thread_Info'][currentThread] = exceptionInfo


if __name__ == '__main__':
    _Run()
