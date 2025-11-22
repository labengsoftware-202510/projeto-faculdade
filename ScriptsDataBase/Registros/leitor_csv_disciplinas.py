import pandas as pd

def retornaTipo(entrada):
    if entrada == 'Obrigatoria':
        return 'O'
    elif entrada == 'Eletiva 1':
        return 'E1'
    elif entrada == 'Eletiva 2':
        return 'E2'
    elif entrada == 'Descontinuada':
        return 'D'
    elif entrada == 'Substituida':
        return 'S'
    else:
        return 'NULL'

def retornAtivo(entrada):
    if entrada == 'ativa':
        return 'Ativo'
    elif entrada == 'inativa':
        return 'Inativo'
    else:
        return 'NULL' 

linhas_processadas = []

try:
    df = pd.read_csv('.\\ScriptsDataBase\\Registros\\disciplinas.csv', sep=',')
    print("DataFrame original:")

except FileNotFoundError:
    print("Erro: O arquivo 'disciplinas.csv' não foi encontrado.")
    print("Por favor, crie um arquivo com esse nome para o exemplo funcionar.")
    exit()

cabecalho = 'insert into disciplinas (nom_dis, dat_inc, tipo, crg_hor_semanal, crg_hor_min_semestral, inativa) values '
linhas_processadas.append(cabecalho)

for index, row in df.iterrows():
    if index == 0:
        linhaNova = f"('{row['nom_dis']}', '{row['dat_inc']}', '{retornaTipo(row['tipo'])}', {row['crg_hor_semanal']}, {row['carga']}, '{retornAtivo(row['inativa'])}')\n"
    else:
        linhaNova = f",('{row['nom_dis']}', '{row['dat_inc']}', '{retornaTipo(row['tipo'])}', {row['crg_hor_semanal']}, {row['carga']}, '{retornAtivo(row['inativa'])}')\n"
    linhas_processadas.append(linhaNova)

print(linhas_processadas)
with open('.\\ScriptsDataBase\\Registros\\insert_disciplinas.sql', 'w') as arquivo_saida:
    arquivo_saida.writelines(linhas_processadas)