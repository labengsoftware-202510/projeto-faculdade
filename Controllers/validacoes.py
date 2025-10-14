import re

def regexCep(entrada):
    regexNotCep = re.compile(r'[^0-9]')
    if regexNotCep.match(entrada):
        return False
    return True