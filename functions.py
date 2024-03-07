# import pandas as pd
from pathlib import Path

def mesclar_panilhas(vendas, lojas):
    vendas =  vendas.merge(lojas, on='ID Loja')
    return vendas


def criar_dicionario_loja(lojas, vendas):
   
    dicionario_lojas = {}
    for loja in lojas['Loja']:
        dicionario_lojas[loja] = vendas.loc[vendas['Loja'] == loja, :]
    
    return dicionario_lojas


def pegar_dia(vendas):
    return vendas['Data'].max()


def criar_pasta_backup(dicionario_lojas, indicador):
    caminho_backup =  Path(r'Backup Arquivos Lojas')
    arquivos_pasta_backup = caminho_backup.iterdir()

    listar_arquivos = [arquivo.name for arquivo in arquivos_pasta_backup]

    for loja in dicionario_lojas:
        if loja not in arquivos_pasta_backup:
            nova_pasta = caminho_backup / loja
            nova_pasta.mkdir(exist_ok=True)

        #Salvar arquivos dentro da pasta
        nome_arquivo = '{}_{}_{}.xlsx'.format(indicador.day, indicador.month, loja)
        local_arquivo = caminho_backup / loja / nome_arquivo
        dicionario_lojas[loja].to_excel(local_arquivo)
