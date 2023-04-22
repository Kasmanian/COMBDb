"""Defines metadata for the application and underlying database."""
from .tables.cats import CAT_TABLE_NAME, CAT_DEFINITION
from .tables.clinicians import CLINICIAN_TABLE_NAME, CLINICIAN_DEFINITION
from .tables.cultures import CULTURE_TABLE_NAME, CULTURE_DEFINITION

TITLE = "COMBDb"

DATABASE_DEFINITION = {
    CAT_TABLE_NAME: CAT_DEFINITION,
    CLINICIAN_TABLE_NAME: CLINICIAN_DEFINITION,
    CULTURE_TABLE_NAME: CULTURE_DEFINITION,
    # IDKEY_TABLE_NAME: IDKEY_DEFINITION,
    # TECH_TABLE_NAME: TECH_DEFINITION,
    # WATERLINE_TABLE_NAME: WATERLINE_DEFINITION,
    # WORDBANK_TABLE_NAME: WORDBANK_DEFINITION,
}
