import os
import sys
import shutil
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from db import Database
from datetime import date

db = Database()


class TestDatabase(unittest.TestCase):


    def test_connect_failed(self):
        isConnected = db.connect('')
        self.assertEqual(isConnected, False, 'Connection should return False')


    def test_connect_passed(self):
        cwd = os.getcwd()
        shutil.copyfile(cwd+r'\COMBDb.accdb', cwd+r'\testing\COMBDb_test.accdb')
        isConnected = db.connect(cwd+r'\testing\COMBDb_test.accdb')
        self.assertEqual(isConnected, True, 'Connection should return True')


    def test_generateSampleID_current_year(self):
        crntYear = date.today().year
        self.sampleID = db.generateSampleID(crntYear)
        self.assertEqual(self.sampleID, f'{crntYear-2000}0001', f'SampleID should be "{crntYear-2000}0001"')


    def test_generateSampleID_next_year(self):
        nextYear = date.today().year+1
        self.sampleID = db.generateSampleID(nextYear)
        self.assertEqual(self.sampleID, f'{nextYear-2000}0001', f'SampleID should be "{nextYear-2000}0001"')


    def test_generateHexID_antibiotic(self):
        self.hexID = {}
        self.hexID['Antibiotic'] = db.generateHexID('Antibiotic')
        self.assertEqual(self.hexID['Antibiotic'], '001', 'HexID should be "001"')


    def test_generateHexID_bacteria(self):
        self.hexID = {}
        self.hexID['Bacteria'] = db.generateHexID('Bacteria')
        self.assertEqual(self.hexID['Bacteria'], '001', 'HexID should be "001"')


    def test_generateHexID_blac(self):
        self.hexID = {}
        self.hexID['B-Lac'] = db.generateHexID('B-lac')
        self.assertEqual(self.hexID['B-Lac'], '1', 'HexID should be "1"')


    def test_generateHexID_growth(self):
        self.hexID = {}
        self.hexID['Growth'] = db.generateHexID('Growth')
        self.assertEqual(self.hexID['Growth'], '1', 'HexID should be "1"')


    def test_generateHexID_susceptibility(self):
        self.hexID = {}
        self.hexID['Susceptibility'] = db.generateHexID('Susceptibility')
        self.assertEqual(self.hexID['Susceptibility'], '1', 'HexID should be "1"')


    def test_single_insert_CAT(self):
        table = '[CATs]'
        fields = (
            '[SampleID]', '[ChartID]', '[Clinician]', '[First]', '[Last]', '[Received]', '[Collected]', '[Reported]',
            '[Volume (ml)]', '[Time (min)]', '[Initial (pH)]', '[Flow Rate (ml/min)]', '[Buffering Capacity (pH)]',
            '[Strep mutans (CFU/ml)]', '[Lactobacillus (CFU/ml)]', '[Tech]', '[Comments]', '[Notes]',
            '[Type]', '[Rejection Date]', '[Rejection Reason]'
        )
        crntDate = date.today()
        sampleID = db.generateSampleID(crntDate.year)
        status = db.insert(
            table, fields, sampleID, '0000a', 0, 'John', 'Doe', crntDate, crntDate, crntDate,
            0, 0, 0, 0, 0, 0, 0, 0, 'Hello', 'World', 'Test', crntDate, 'N/A'
        )
        self.assertEqual(status, True, 'Insert should return "True"')


    def test_single_insert_culture(self):
        table = '[Cultures]'
        fields = (
            '[SampleID]', '[ChartID]', '[Clinician]', '[First]', '[Last]', 
            '[Received]', '[Collected]', '[Reported]', '[Aerobic Results]', '[Anaerobic Results]',
            '[Tech]', '[Comments]', '[Notes]', '[Type]', '[Direct Smear]', '[Rejection Date]', '[Rejection Reason]'
        )
        crntDate = date.today()
        sampleID = db.generateSampleID(crntDate.year)
        status = db.insert(
            table, fields, sampleID, '0000a', 0, 'John', 'Doe', crntDate, crntDate, crntDate,
            'N/A', 'N/A', 0, 'Hello', 'World', 'Test', '...', crntDate, 'N/A'
        )
        self.assertEqual(status, True, 'Insert should return "True"')


    def test_single_insert_waterline(self):
        table = '[Waterlines]'
        fields = (
            '[SampleID]', '[ChartID]', '[Clinician]', '[First]', '[Last]', 
            '[Received]', '[Collected]', '[Reported]', '[Aerobic Results]', '[Anaerobic Results]',
            '[Tech]', '[Comments]', '[Notes]', '[Type]', '[Direct Smear]', '[Rejection Date]', '[Rejection Reason]'
        )
        crntDate = date.today()
        sampleID = db.generateSampleID(crntDate.year)
        status = db.insert(
            table, fields, sampleID, '0000a', 0, 'John', 'Doe', crntDate, crntDate, crntDate,
            'N/A', 'N/A', 0, 'Hello', 'World', 'Test', '...', crntDate, 'N/A'
        )
        self.assertEqual(status, True, 'Insert should return "True"')


if __name__ == '__main__':
    unittest.main()
    db.close()
