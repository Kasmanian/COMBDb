"""Table for caries activity tests."""
from .__utils import *

# table definition
CAT_TABLE_NAME = "CATs"
CAT_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "SampleID": "VARCHAR",
    # Short Text: string conversion of the sample #, formatted as yy####
    "ChartID": "VARCHAR",
    # Short Text: unique string ID of the patient
    "Type": "VARCHAR",
    # Short Text: ???
    "First": "VARCHAR",
    # Short Text: first name of the patient
    "Last": "VARCHAR",
    # Short Text: last name of the patient
    "Clinician": "INTEGER",
    # Number: 'Entry' field of the clinician (from Clinicians table)
    "Collected": "DATETIME",
    # Date/Time: date the sample was collected
    "Tech": "INTEGER",
    # Number: 'Entry' field of this entry's last editing tech (from Techs table)
    "Received": "DATETIME",
    # Date/Time: date the sample was received
    "Reported": "DATETIME",
    # Date/TIme: date the sample was reported
    "Volume (ml)": "DECIMAL",
    # Number: volume recorded in milliliters
    "Time (min)": "DECIMAL",
    # Number: time recorded in minutes
    "Initial (pH)": "DECIMAL",
    # Number: initial pH
    "Flow Rate (ml/min)": "DECIMAL",
    # Number: volume/time recorded in milliliters per minutes
    "Buffering Capacity (pH)": "DECIMAL",
    # Number: buffering capacity recorded in pH
    "Strep mutans (CFU/ml)": "INTEGER",
    # Number: count of Strep mutans recorded in colony-forming units per milliliter
    "Lactobacillus (CFU/ml)": "INTEGER",
    # Number: count of Lactobacillus recorded in colony-forming units per milliliter
    "Comments": "LONGCHAR",
    # Long Text: comments to be seen on printed reports
    "Notes": "LONGCHAR",
    # Long Text: notes to be seen internally or on order forms
    "Rejection Date": "DATETIME",
    # Date/Time: date of rejection
    "Rejection Reason": "LONGCHAR",
    # Long Text: explanation for rejection
}
CAT_TABLE_COLUMNS = tuple(CAT_DEFINITION.keys())

# field subsets
CAT_ORDER_FIELDS_SUBSET = QWARG_FORMAT(CAT_TABLE_COLUMNS[1:8])
CAT_ALL_FIELDS_SUBSET = QWARG_FORMAT(CAT_TABLE_COLUMNS)
CAT_RESULTS_FIELDS_SUBSET = CAT_ALL_FIELDS_SUBSET[1:]
