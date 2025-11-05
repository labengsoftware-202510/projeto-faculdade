import re

regexCep = re.compile(r'\d{5}-\d{3}')
regexCepNum = re.compile(r'\d{8}')

regexCpf = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
regexCpfNum = re.compile(r'\d{11}')

def vCep(entrada):
    if regexCep.match(entrada):
        return True
    return False

def vCepNum(entrada):
    if regexCepNum.match(entrada):
        return True
    return False

def vCpf(entrada):
    if regexCpf.match(entrada):
        return True
    return False

def vCpfNum(entrada):
    if regexCpfNum.match(entrada):
        return True
    return False