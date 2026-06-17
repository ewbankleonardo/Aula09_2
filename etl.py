import pandas as pd
import os
import glob
from loguru import logger
from utils_log import log_decorator

@log_decorator
def extrair_dados_e_consolidar(pasta:str) -> pd.DataFrame:
    #listar o que está na pasta e termina com .json
    #retorna uma lista com os arquivos .json na pasta
    arquivos_json = glob.glob(os.path.join(pasta,"*.json")) 

    #cria uma lista de data frames a partir dos arquivos lidos
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    #concatenar dfs, unir todos os dfs que tem o mesmo schema
    df_total = pd.concat(df_list,ignore_index=True)

    return df_total
@log_decorator

def calcular_kpi_de_total_de_vendas(df:pd.DataFrame)->pd.DataFrame:
    #adicionar uma coluna vendas*quantidade pra obter o total
    df["Total"] = df["Quantidade"]*df["Venda"]
    return df
@log_decorator
def salvar_dados(formato_saida, df):
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('data/output.csv',index=False,encoding='utf-8')
        if formato == 'parquet':
            df.to_parquet('data/output.parquet')

          #  Append the DataFrame: 
          # df.to_csv('existing.csv', mode='a', index=False, header=False)
@log_decorator
def pipeline_kpi_vendas_consolidado(pasta:str,formato_saida:list):
    formato_saida:list=["csv","parquet"]
    df=extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df)
    salvar_dados(formato_saida,df_calculado)