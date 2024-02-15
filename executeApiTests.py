import argparse
import pytest

from config.configManager import ConfigManager
from utils.enum import Environment
from utils import SetupCalls

def parse_args():
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
   
    args = parser.parse_args()
    return args

def run():
    """
    Run from command line.

    Returns
    -------
    """

    _args = parse_args()
    environment = Environment.from_str(_args.env)

    SetupCalls.SetUpLogging()
    ConfigManager.InitializeConfig(
        env = environment)
    pytest.main(["tests", "--junitxml=./test-results/report.xml"])
    

if __name__ == '__main__':
    run()
