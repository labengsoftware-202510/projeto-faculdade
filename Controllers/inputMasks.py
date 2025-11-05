import Controllers.validacoes as validacoes

def cepMask(cep):
    if validacoes.vCepNum(cep):
        return f'{cep[:5]}-{cep[5:]}'
    elif validacoes.vCep(cep):
        return cep
    else:
        return ''
    
def cepUnmask(cep):
    if validacoes.vCep(cep) or validacoes.vCepNum(cep):
        return cep.replace('-','')
    else:
        return  ''
    
def cpfMask(cpf):
    if validacoes.vCpfNum(cpf):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    elif validacoes.vCpf(cpf):
        return cpf
    else:
        return ''

def cpfUnmask(cpf):
    if validacoes.vCpf(cpf) or validacoes.vCpfNum(cpf):
        return cpf.replace('.','').replace('-','')
    else:
        return ''