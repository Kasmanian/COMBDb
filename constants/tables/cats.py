from .__utils import *

# table definition
CAT_TABLE_NAME = "CATs"
CAT_RAW_FIELDS = (
    "Entry",
    # AutoNumber: unique incrementing entry #
    "SampleID",
    # Short Text: string conversion of the sample #, formatted as yy####
    "ChartID",
    # Short Text: unique string ID of the patient
    "Clinician",
    # Number: 'Entry' field of the clinician (from Clinician table)
    "First",
    # Short Text: first name of the patient
    "Last",
    # Short Text: last name of the patient
    "Tech",
    # Number: 'Entry' field of this entry's last editing tech (from Tech table)
    "Collected",
    # Date/Time: date the sample was collected
    "Received",
    # Date/Time: date the sample was received
    "Reported",
    # Date/TIme: date the sample was reported
    "Volume (ml)",
    # Number: volume recorded in milliliters
    "Time (min)",
    # Number: time recorded in minutes
    "Initial (pH)",
    # Number: initial pH
    "Flow Rate (ml/min)",
    # Number: volume/time recorded in milliliters per minutes
    "Buffering Capacity (pH)",
    # Number: buffering capacity recorded in pH
    "Strep mutans (CFU/ml)",
    # Number: count of Strep mutans recorded in colony-forming units per milliliter
    "Lactobacillus (CFU/ml)",
    # Number: count of Lactobacillus recorded in colony-forming units per milliliter
    "Comments",
    # Long Text: comments to be seen on printed reports
    "Notes",
    # Long Text: notes to be seen internally or on order forms
    "Type",
    # Short Text: ???
    "Rejection Date",
    # Date/Time: date of rejection
    "Rejection Reason",
    # Long Text: explanation for rejection
)

# field subsets
CAT_ORDER_FIELDS_SUBSET = QWARG_FORMAT(CAT_RAW_FIELDS[1:6])
CAT_ALL_FIELDS_SUBSET = QWARG_FORMAT(CAT_RAW_FIELDS)
CAT_RESULTS_FIELDS_SUBSET = CAT_ALL_FIELDS_SUBSET[1:]
