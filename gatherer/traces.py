from datetime import datetime
from inspect import currentframe, getframeinfo, getouterframes, stack

DATETIME_FORMAT = '%b-%d-%Y %I:%M:%S %p'


def prefix(level: str = 'DEBUG') -> str:
    """Replicates the logging config to print colored statements accordingly.

    Args:
        level: Takes the log level as an argument.

    Returns:
        str:
        A well formatted prefix to be added before a print statement.
    """
    calling_file = getouterframes(currentframe(), 2)[1][1].split('/')[-1].rstrip('.py')
    return f"{datetime.now().strftime(DATETIME_FORMAT)} - {level} - [{calling_file}:" \
           f"{getframeinfo(stack()[1][0]).lineno}] - {stack()[1].function} - "
