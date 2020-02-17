import inspect
import sys
import re


def execute_string():
    code = inspect.getsourcelines(sys.modules[__name__])[0]
    cleaned = ''
    for i, l in enumerate(code):
        if i in range(14, 30):
            cleaned += l
    exec(re.sub(r'\t{4}', '', cleaned))


def insert_middle():
    original = 'Ram Verma'
    mid = 0
    listed = list(original)
    length = len(listed)
    i = (length - 1) // 2

    # If length is odd
    if length % 2:
        altered = original[:i] + ' Kumar ' + original[i:]
    else:
        altered = original[:i + 1] + ' kumar ' + original[i + 1:]
    print(altered)


insert_middle()

execute_string()