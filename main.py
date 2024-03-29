import pandas as pd
from functions import *
from pathlib import Path



def main():
    
    emails_df = pd.read_excel(r'Bases de Dados\Emails.xlsx')
    lojas_df =  pd.read_csv(r'Bases de Dados\Lojas.csv', encoding='latin1', sep=';')
    vendas_df = pd.read_excel(r'Bases de Dados\Vendas.xlsx')

    caminho_diretorio = Path(r"Arquivos Lojas")

    

    #Juntando a tabela de vendas com a de Lojas
    vendas = mesclar_panilhas(vendas_df, lojas_df)

    #Criar um dicionarios para as lojas
    dicionario_lojas = criar_dicionario_loja(lojas_df, vendas)

    #Sempre pegar o maior dia 
    indicador_dia = pegar_dia(vendas)

    #Se a pasta Arquivos lojas não existe, ela vai ser criada
    if not caminho_diretorio.is_dir():
        # Cria o diretório se não existir
        caminho_diretorio.mkdir(parents=True, exist_ok=True)
    
    #Criar as pastas das Lojas dentro da pasta backup arquivo Lojas
    criar_pasta_backup(dicionario_lojas, indicador_dia)
    


if __name__ == '__main__':
    main()
