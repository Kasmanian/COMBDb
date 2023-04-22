"""Table for technician user information."""
from .__utils import *

# table definition
TECH_TABLE_NAME = "Techs"
TECH_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "First": "VARCHAR",
    # Short Text: first name of the technician
    "Middle": "VARCHAR",
    # Short Text: middle name or inital of the technician
    "Last": "VARCHAR",
    # Short Text: last name of the technician
    "Username": "VARCHAR",
    # Short Text: username of the technician
    "Password": "LONGCHAR",
    # Long Text: password of the technician
    "Active": "VARCHAR",
    # Short Text: yes/no, whether the technician's account is active or not
}
TECH_TABLE_COLUMNS = tuple(TECH_DEFINITION.keys())

# field subsets
TECH_ALL_FIELDS_SUBSET = QWARG_FORMAT(TECH_TABLE_COLUMNS)
