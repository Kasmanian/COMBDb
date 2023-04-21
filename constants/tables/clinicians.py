from .__utils import *

# table definition
CLINICIAN_TABLE_NAME = 'Clinicians'
CLINICIAN_RAW_FIELDS = [
    'Entry', # AutoNumber: unique incrementing entry #
    'First', # Short Text: first name of the clinician
    'Last', # Short Text: last name of the clinician
    'Prefix', # Short Text: title of the clinician
    'Phone', # Short Text: phone number of clinician or designation
    'Fax', # Short Text: fax of the clinician or designation
    'Designation', # Short Text: name of the clinic or clinician's place of practice
    'Address 1', # Short Text: first address line of designation
    'Address 2', # Short Text: second address line of designation
    'City', # Short Text: city of designation
    'State', # Short Text: state of designation
    'Zip', # Short Text: zip of designation
    'Email', # Short Text: email of clinician or designation
    'Enrolled', # Date/Time: date of enrollment of clinician
    'Inactive', # Date/Time: date of deactivation of clinician
    'Comments', # Long Text: comments on clinician
    'OldID', # Number: reference to the clinician's old ID in the old database
]

# field subsets
CLINICIAN_NAME_SUBSET = CLINICIAN_RAW_FIELDS[0:3]

# query definitions
# DROPDOWN_QWARGS = QWARG_FORMAT(NAME, NAME_SUBSET)
# ALL_QWARGS = QWARG_FORMAT(NAME, FIELDS)
