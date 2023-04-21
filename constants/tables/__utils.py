'''Defines helper methods used by the table modules.'''

def QWARG_FORMAT(fieldsTuple: tuple):
    '''Formats query arguments for database consumption.

    Parameters:
      fieldsList: list of fields to be queried

    Returns:
      formatted query arguments
    '''
    return tuple(map(lambda field: f'[{field}]', fieldsTuple))
