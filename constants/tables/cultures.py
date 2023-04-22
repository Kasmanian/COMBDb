"""Table for non-CAT cultures."""
from .__utils import *

# table definition
CULTURE_TABLE_NAME = "CATs"
CULTURE_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "SampleID": "VARCHAR",
    # Short Text: string conversion of the sample #, formatted as yy####
    "ChartID": "VARCHAR",
    # Short Text: unique string ID of the patient
    "Type": "VARCHAR",
    # Short Text: type of culture being tested
    "First": "VARCHAR",
    # Short Text: first name of the patient
    "Last": "VARCHAR",
    # Short Text: last name of the patient
    "Clinician": "INTEGER",
    # Number: 'Entry' field of the clinician (from Clinician table)
    "Collected": "DATETIME",
    # Date/Time: date the sample was collected
    "Tech": "INTEGER",
    # Number: 'Entry' field of this entry's last editing tech (from Tech table)
    "Received": "DATETIME",
    # Date/Time: date the sample was received
    "Reported": "DATETIME",
    # Date/TIme: date the sample was reported
    "Aerobic Results": "LONGCHAR",
    # Long Text: codified string of aerobic bacteria and antibiotics observed/tested
    "Aerotolerant Results": "LONGCHAR",
    # Long Text: codified string of aerotolerant bacteria and antibiotics observed/tested
    "Comments": "LONGCHAR",
    # Long Text: comments to be seen on printed reports
    "Notes": "LONGCHAR",
    # Long Text: notes to be seen internally or on order forms
    "Direct Smear": "LONGCHAR",
    # Long Text: comments related specifically to direct smear testing
    "Rejection Date": "DATETIME",
    # Date/Time: date of rejection
    "Rejection Reason": "LONGCHAR",
    # Long Text: explanation for rejection
}
CULTURE_TABLE_COLUMNS = tuple(CULTURE_DEFINITION.keys())

# field subsets
CULTURE_ORDER_FIELDS_SUBSET = QWARG_FORMAT(CULTURE_TABLE_COLUMNS[1:8])
CULTURE_ALL_FIELDS_SUBSET = QWARG_FORMAT(CULTURE_TABLE_COLUMNS)
CULTURE_RESULTS_FIELDS_SUBSET = CULTURE_ALL_FIELDS_SUBSET[1:]
