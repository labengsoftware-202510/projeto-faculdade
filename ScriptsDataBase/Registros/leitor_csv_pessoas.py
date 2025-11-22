import pandas as pd
import random

def retornAtivo(entrada):
    if entrada == 'ativo':
        return 'Ativo'
    elif entrada == 'inativo':
        return 'Inativo'
    else:
        return 'NULL' 

def gerarCategoria():
    categorias = [1, 2, 3, 4]
    return random.choice(categorias)

linhas_processadas = []

try:
    df = pd.read_csv('.\\ScriptsDataBase\\Registros\\pessoas.csv', sep=',')
    print("DataFrame original:")
    print(df.head())

except FileNotFoundError:
    print("Erro: O arquivo 'disciplinas.csv' não foi encontrado.")
    print("Por favor, crie um arquivo com esse nome para o exemplo funcionar.")
    exit()

cabecalho = 'insert into pessoas (nom_com, cpf, dat_nas, categoria, cep, num, comp, sit) values '
linhas_processadas.append(cabecalho)

for index, row in df.iterrows():
    if index == 0:
        linhaNova = f"('{row['nom_com']}', {row['cpf']}, '{row['dat_nas']}', {gerarCategoria()}, {row['cep']}, {row['num']}, '{row['comp'] if row['comp'] else ''}', '{retornAtivo(row['sit'])}')\n"
    else:
        linhaNova = f",('{row['nom_com']}', {row['cpf']}, '{row['dat_nas']}', {gerarCategoria()}, {row['cep']}, {row['num']}, '{row['comp'] if row['comp'] else ''}', '{retornAtivo(row['sit'])}')\n"
    linhas_processadas.append(linhaNova)

print(linhas_processadas)
with open('.\\ScriptsDataBase\\Registros\\insert_pessoas.sql', 'w') as arquivo_saida:
    arquivo_saida.writelines(linhas_processadas)