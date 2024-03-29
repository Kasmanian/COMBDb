APP_ERROR_CODES = [
    None,  # 0
    "Unexpected",  # 1
]

DATABASE_ERROR_CODES = [
    None,  # 0
    "Unexpected",  # 1
    "Invalid database file",  # 2
    "INSERT failed",  # 3
    "UPDATE failed",  # 4
    "SELECT failed",  # 5
    "Database validation interrupted",  # 6
]

DATABASE_ERROR_KEYS = {
    "insert": 3,
    "update": 4,
    "select": 5,
    "validate": 6,
}
