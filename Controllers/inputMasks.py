import re

def cepMask (entrada):
    regexNotCep = re.compile(r'[^0-9]')
    if regexNotCep.match(entrada):
        ...
    saidaMask = ''
    if entrada:
        for l in entrada:
            if l not in '':
                ...
    else:
        saidaMask = '_____-___'
    return saidaMask