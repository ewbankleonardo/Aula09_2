from etl import pipeline_kpi_vendas_consolidado

#esse arquivo serve pro usuário usar a pipeline criada, sem modificar o código
#analista só tem que alterar a pasta e o tipo de saida, facilitando o trabalho
#

pasta = 'data'
formato_saida = ["csv"]

pipeline_kpi_vendas_consolidado(pasta,formato_saida)