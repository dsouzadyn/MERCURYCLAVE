from __future__ import print_function

import re


def print_error(err):
    print("[ERROR]", err)


def print_info(inf):
    print("[INFO]", inf)


def is_valid_b64(s):
    validator = re.compile(
        '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
    if validator.match(s) != None:
        return True
    else:
        return False


def is_valid_ascii(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
