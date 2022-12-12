import os
import shutil
import unittest

from db import Database
from datetime import date

db = Database()


class TestDatabase(unittest.TestCase):


    def test_connect_failed(self):
        isConnected = db.connect('')
        self.assertEqual(isConnected, False, 'Connection should return False')


    def test_connect_passed(self):
        cwd = os.getcwd()
        shutil.copyfile(cwd+r'\COMBDb\COMBDb.accdb', cwd+r'\COMBDb\COMBDb_test.accdb')
        isConnected = db.connect(cwd+r'\COMBDb\COMBDb_test.accdb')
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


if __name__ == '__main__':
    unittest.main()
    db.close()
