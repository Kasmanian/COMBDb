"""Table for contextual words used in reporting, such as names of bacteria and antibiotics."""
from .__utils import *

# table definition
WORDBANK_TABLE_NAME = "Wordbank"
WORDBANK_DEFINITION = {
    "Entry": "COUNTER",
    # AutoNumber: unique incrementing entry #
    "HexID": "VARCHAR",
    # Short Text: unique hexadecimal ID of the word
    "Type": "VARCHAR",
    # Short Text: the category that the word belongs to
    "List": "VARCHAR",
    # Short Text: the name of the list that the word belongs to
    "Prefix": "VARCHAR",
    # Short Text: the word's abbreviation
    "Word": "LONGCHAR",
    # Long Text: the word itself
}
WORDBANK_TABLE_COLUMNS = tuple(WORDBANK_DEFINITION.keys())

# field subsets
WORDBANK_ALL_FIELDS_SUBSET = QWARG_FORMAT(WORDBANK_TABLE_COLUMNS)
WORDBANK_MAIN_FIELDS_SUBSET = WORDBANK_ALL_FIELDS_SUBSET[1:]
