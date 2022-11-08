# Example of a custom module to be imported

import re              # re = Regular expression module


def validate_email(email):
    if len(email) > 7:
        # Match method checks the signs of an email by regular expressions
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


def validate_email2(mailing):
    if len(mailing) > 7:
        return bool(re.match("([a-zA-Z0-9_\-\.])+@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)", mailing))
