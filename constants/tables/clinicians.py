"""Table for clients and clinicians."""
from .__utils import *

# table definition
CLINICIAN_TABLE_NAME = "Clinicians"
CLINICIAN_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "Title": "VARCHAR",
    # Short Text: title of the clinician
    "First": "VARCHAR",
    # Short Text: first name of the clinician
    "Last": "VARCHAR",
    # Short Text: last name of the clinician
    "Phone": "VARCHAR",
    # Short Text: phone number of clinician or designation
    "Fax": "VARCHAR",
    # Short Text: fax of the clinician or designation
    "Designation": "VARCHAR",
    # Short Text: name of the clinic or clinician's place of practice
    "Address 1": "VARCHAR",
    # Short Text: first address line of designation
    "Address 2": "VARCHAR",
    # Short Text: second address line of designation
    "City": "VARCHAR",
    # Short Text: city of designation
    "State": "VARCHAR",
    # Short Text: state of designation
    "Zip": "VARCHAR",
    # Short Text: zip of designation
    "Email": "VARCHAR",
    # Short Text: email of clinician or designation
    "Enrolled": "DATETIME",
    # Date/Time: date of enrollment of clinician
    "Inactive": "DATETIME",
    # Date/Time: date of deactivation of clinician
    "Comments": "LONGCHAR",
    # Long Text: comments on clinician
    "OldID": "INTEGER",
    # Number: reference to the clinician's old ID in the old database
}
CLINICIAN_TABLE_COLUMNS = tuple(CLINICIAN_DEFINITION.keys())

# field subsets
CLINICIAN_NAME_SUBSET = QWARG_FORMAT(CLINICIAN_TABLE_COLUMNS[0:3])
CLINICIAN_ALL_FIELDS_SUBSET = QWARG_FORMAT(CLINICIAN_TABLE_COLUMNS)
