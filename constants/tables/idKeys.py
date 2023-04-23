"""Table for unique, incremented IDs to be fetched."""
from .__utils import *

# table definition
IDKEY_TABLE_NAME = "IDKeys"
IDKEY_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "Type": "LONGCHAR",
    # Long Text: category for which the key is made for
    "ID": "LONGCHAR",
    # Long Text: string value of the next available ID
}
IDKEY_TABLE_COLUMNS = tuple(IDKEY_DEFINITION.keys())

# field subsets
IDKEY_ALL_FIELDS_SUBSET = QWARG_FORMAT(IDKEY_TABLE_COLUMNS)
IDKEY_MAIN_FIELDS_SUBSET = IDKEY_ALL_FIELDS_SUBSET[1:]
