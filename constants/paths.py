'''Defines common paths used by the application.'''
import os
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

CWD = os.getcwd()
ENVAR_PATH = CWD+r'\workspace\envar.json'
ACCDB_PATH = CWD+r'\COMBDb.accdb'
ACCDB_TEST_PATH = CWD+r'\tests\COMBDb_test.accdb'
