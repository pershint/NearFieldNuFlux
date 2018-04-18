# Here we will put in the argparser commands for main that will be imported.
import argparse
import sys, os

basepath = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description='Parser for near-field reactor flux calculating tool')

##---------------------MAIN RUN FLAGS---------------------##
parser.add_argument('--debug', dest='DEBUG',action='store_true',
        help='Run in debug mode and get some extra outputs and stuff')
parser.add_argument('--buildSB', dest='BUILD', action='store_true',
        help='take files from a WATCHMAKERS data directory (specified with the'+\
                "--datadir flag) and prepare signal/background root files for"+\
                "the TMVA")
parser.set_defaults(DEBUG=False,BUILD=False)

def checkParserInput(argin):
    if argin.DEBUG is True:
        print("ENTERING DEBUGGING MODE...")

args = parser.parse_args()
checkParserInput(args)

