import shutil
import unittest
from datetime import date

from __context import constants as const

from database import Database

db = Database()


class TestDatabase(unittest.TestCase):

    def test_connect_failed(self):
        isConnected = db.connect('')
        self.assertEqual(isConnected, False, 'Connection should return False')

    def test_connect_passed(self):
        shutil.copyfile(const.ACCDB_PATH, const.ACCDB_TEST_PATH)
        isConnected = db.connect(const.ACCDB_TEST_PATH)
        self.assertEqual(isConnected, True, 'Connection should return <True>')

    def test_generateSampleID_current_year(self):
        crntYear = date.today().year
        self.sampleID = db.generateSampleID(crntYear)
        self.assertEqual(
            self.sampleID, f'{crntYear-2000}0001', f'SampleID should be <{crntYear-2000}0001>')

    def test_generateSampleID_next_year(self):
        nextYear = date.today().year+1
        self.sampleID = db.generateSampleID(nextYear)
        self.assertEqual(
            self.sampleID, f'{nextYear-2000}0001', f'SampleID should be <{nextYear-2000}0001>')

    def test_generateHexID_antibiotic(self):
        self.hexID = {}
        self.hexID['Antibiotic'] = db.generateHexID('Antibiotic')
        self.assertEqual(self.hexID['Antibiotic'],
                         '001', 'HexID should be <001>')

    def test_generateHexID_bacteria(self):
        self.hexID = {}
        self.hexID['Bacteria'] = db.generateHexID('Bacteria')
        self.assertEqual(self.hexID['Bacteria'],
                         '001', 'HexID should be <001>')

    def test_generateHexID_blac(self):
        self.hexID = {}
        self.hexID['B-Lac'] = db.generateHexID('B-lac')
        self.assertEqual(self.hexID['B-Lac'], '1', 'HexID should be <1>')

    def test_generateHexID_growth(self):
        self.hexID = {}
        self.hexID['Growth'] = db.generateHexID('Growth')
        self.assertEqual(self.hexID['Growth'], '1', 'HexID should be <1>')

    def test_generateHexID_susceptibility(self):
        self.hexID = {}
        self.hexID['Susceptibility'] = db.generateHexID('Susceptibility')
        self.assertEqual(self.hexID['Susceptibility'],
                         '1', 'HexID should be <1>')

    def test_single_insert_CAT(self):
        crntDate = date.today()
        sampleID = db.generateSampleID(crntDate.year)
        status = db.insert(
            const.CAT_TABLE_NAME, const.CAT_RESULTS_FIELDS_SUBSET, sampleID, '0000a', 0, 'John', 'Doe',
            crntDate, crntDate, crntDate, 0, 0, 0, 0, 0, 0, 0, 0, 'Hello', 'World', 'Test', crntDate, 'N/A')
        self.assertEqual(status, True, 'Insert should return <True>')

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

    # def test_single_insert_waterline(self):
    #     table = '[Waterlines]'
    #     fields = (
    #         '[SampleID]', '[ChartID]', '[Clinician]', '[First]', '[Last]',
    #         '[Received]', '[Collected]', '[Reported]', '[Aerobic Results]', '[Anaerobic Results]',
    #         '[Tech]', '[Comments]', '[Notes]', '[Type]', '[Direct Smear]', '[Rejection Date]', '[Rejection Reason]'
    #     )
    #     crntDate = date.today()
    #     sampleID = db.generateSampleID(crntDate.year)
    #     status = db.insert(
    #         table, fields, sampleID, '0000a', 0, 'John', 'Doe', crntDate, crntDate, crntDate,
    #         'N/A', 'N/A', 0, 'Hello', 'World', 'Test', '...', crntDate, 'N/A'
    #     )
    #     self.assertEqual(status, True, 'Insert should return "True"')


if __name__ == '__main__':
    unittest.main()
    db.close()
