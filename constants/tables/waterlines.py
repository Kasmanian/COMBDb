"""Table for waterlines."""
from .__utils import *

# table definition
WATERLINE_TABLE_NAME = "Waterlines"
WATERLINE_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "SampleID": "VARCHAR",
    # Short Text: string conversion of the sample #, formatted as yy####
    "OperatoryID": "VARCHAR",
    # Short Text: unique string ID of the waterline
    "Clinician": "INTEGER",
    # Number: 'Entry' field of the clinician (from Clinicians table)
    "Collected": "DATETIME",
    # Date/Time: date the sample was collected
    "Shipped": "DATETIME",
    # Date/Time: date the sample was shipped
    "Tech": "INTEGER",
    # Number: 'Entry' field of this entry's last editing tech (from Techs table)
    "Received": "DATETIME",
    # Date/Time: date the sample was received
    "Reported": "DATETIME",
    # Date/TIme: date the sample was reported
    "Product": "VARCHAR",
    # Short Text: product used to clean the waterline
    "Procedure": "VARCHAR",
    # Short Text: method used to clean the waterline
    "Bacteria Count": "INTEGER",
    # Number: amount of bacteria observed in the sample
    "CDC/ADA": "VARCHAR",
    # Short Text: note on how the sample compares to CDC/ADA standards
    "Comments": "LONGCHAR",
    # Long Text: comments to be seen on printed reports
    "Notes": "LONGCHAR",
    # Long Text: notes to be seen internally or on order forms
    "Rejection Date": "DATETIME",
    # Date/Time: date of rejection
    "Rejection Reason": "LONGCHAR",
    # Long Text: explanation for rejection
}
WATERLINE_TABLE_COLUMNS = tuple(WATERLINE_DEFINITION.keys())

# field subsets
WATERLINE_RECEIVING_FIELDS_SUBSET = QWARG_FORMAT(WATERLINE_TABLE_COLUMNS[1:8])
WATERLINE_ORDER_FIELDS_SUBSET = QWARG_FORMAT(WATERLINE_TABLE_COLUMNS[1:8])
WATERLINE_ALL_FIELDS_SUBSET = QWARG_FORMAT(WATERLINE_TABLE_COLUMNS)
WATERLINE_RESULTS_FIELDS_SUBSET = WATERLINE_ALL_FIELDS_SUBSET[1:]
