import pytest

import re

def phone_numbers(values):
    return re.findall(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}', values)
