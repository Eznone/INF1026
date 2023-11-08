"""
Algumas das questoes e possiveis solucoes
Nao sofreu revisao e pode conter erros
Nem todas as questoes do teste foram consideradas
"""
import pandas as pd
import matplotlib.pyplot as plt

import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'cadastroempresas2020.xlsx'
path = os.path.join(pre, fname)

pd.set_option("display.max_rows",200)
pd.set_option("display.max_columns",100)

'''
O arquivo cadastroempresas2020.xlsx armazena informações de algumas empresas
nas seguintes planilhas:
   
A planilha dados:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    AreaAtividade: área de atuação da empresa. Por exemplo, uma academia ou
                   centro esportivo atua na área de ESPORTES
    NumeroDeUnidades: quantidade de filiais da empresa
    QtdDeFuncionarios: número de funcionários considerando todas as filiais
    SalarioMedio: salário médio dos funcionários, medido em número de
                  salários mínimos
    AnoDeCriacao: ano de fundação da empresa
   
A planilha desempenho:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    Lucro2017: faturamento líquido no ano de 2017, em mil reais
    Lucro2018: faturamento líquido no ano de 2018, em mil reais      
    Lucro2019: faturamento líquido no ano de 2019, em mil reais
   
A planilha situação
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente        
    SituacaoFiscal: situação fiscal ( REGULAR ou IRREGULAR) no ano atual
'''

dfDados=pd.read_excel(path,sheet_name='Dados',index_col=0,header=0)

dfLucro=pd.read_excel(path,sheet_name='Desempenho',index_col=0,header=0)

dfSit=pd.read_excel(path,sheet_name='SituacaoFiscal',index_col=0,header=0)



print('\n--------------------dfDados----------------------------')
print(dfDados)
print('\n--------------------dfLucro-----------------------------')
print(dfLucro)
print('\n---------------------dfSit------------------------------')
print(dfSit)
print('\n--------------------------------------------------------')

#======================================================================
print('\n==================================================================')
#Questao1:
# Conhecendo os DataFrames:
print('\nQuestao1:')
#  1A) dfDados: Exiba o percentual de empresas com mais de 20 funcionários e
#               que tenham até 10 filiais
#  1B) dfLucro: Exiba o percentual de valores ausentes
#  1C) dfSit:   Exiba os 4 últimos elementos ordenados por NomeDaEmpresa'
#  1D) dfDados: Exiba os 8 primeiros elementos ordenados por NumeroDeUnidades/QtdDeFuncionarios
#  1E) dfLucro: Exiba o percentual de empresas cujo lucro em 2018 foi superior ao lucro de 2019
#  1F) dfSit:   Exiba a situação das empresas Fominha,KurtExames e VemSerFit

print('\n1A -dfDados: perc de empresas > 20 funcionarios e com ate  10 filiais ')
empresa10Filiais = dfDados.loc[(dfDados.NumeroDeUnidades <= 10) & (dfDados.QtdDeFuncionarios > 20)]
tp = empresa10Filiais.size/dfDados.size*100
print(tp)

print('\n1B) dfLucro: Exiba o percentual de valores ausentes ')
valoresAusentes = dfLucro.isnull().sum().sum()
tpValAus = valoresAusentes/dfLucro.size*100
print(tpValAus)

print('\n1C) dfSit:   Exiba os 4 últimos elementos ordenados por NomeDaEmpresa')
print(dfSit.sort_index().tail(4))

print('\n1D) dfDados: os 8 prim ordenados por NumeroDeUnidades/QtdDeFuncionarios ')
print(dfDados.sort_values(by=['NumeroDeUnidades','QtdDeFuncionarios']).head(8))

print('\n1E) dfLucro: percentual de empresas com lucro em 2018 > lucro de 2019  ')
LucroMaior19 = dfLucro.loc[dfLucro.LUCRO2018 > dfLucro.LUCRO2019]
tpLucro = LucroMaior19.size/dfLucro.size*100
print(tpLucro)

print('\nExtra1: DF com as empresas com lucro maior em 18')
print(LucroMaior19)

print('\nExtra2: So nome das empresas com lucro maior em 18')
print(LucroMaior19.index.values)

print('\n1F) dfSit:   Exiba a situação das empresas Fominha,KurtExames e VemSerFit')
print(dfSit.loc[['Fominha','KurtExames' , 'VemSerFit']])

#======================================================================
print('\n=========================================================')


#Questao2:
#  Consertando os Dataframes :

# Consertando os Dataframes
#      dfDados: valores ausentes na coluna NumeroDeUnidades devem ser
#               substituídos pela média da coluna',
#      dfDados: valores ausentes na coluna SalarioMedio devem ser
#               substituídos pelo menor valor de empresas de mesma área
#               de atividade
#      dfDados: renomeie as colunas para que sejam identificadas por
#               rótulos com até 6 caracteres, todos maiúsculos',


# OBS: o numero de unidades deve ser um inteiro

print('\n*********************************************')
print('******************  Q2  ********************')
print('*********************************************')
print('\nNovo dfDados')
dfDados.NumeroDeUnidades.fillna(int(dfDados.NumeroDeUnidades.mean()),axis=0,inplace=True)
dfDados.SalarioMedio.fillna(dfDados.SalarioMedio.min(),axis=0,inplace=True)
#dfDados.rename(columns={'AreaAtividade':'ARATIV','NumeroDeUnidades':'NUMUNI','QtdDeFuncionarios':'QTDFUN','SalarioMedio':'SALMED','AnoDeCriacao':'ANOCRI'},inplace=True)
print(dfDados)

print('\n*********************************************')

#      dfLucro: substitua os valores ausentes de cada empresa pelo lucro
#               mediano da empresa,
#      dfLucro: inclua a coluna LUCRO com o maior lucro nos 3 anos
#               de cada empresa


print('\nPreenchidos usando DF transposto')
#MELHOR FORMA: trabalhar com DF transposto
dfLucro.T.fillna(dfLucro.median(axis=1),inplace=True)
print(dfLucro)

print('\n*********************************************')
dfLucro['MaiorLucro'] = dfLucro.max(axis=1)
print(dfLucro)

print('\n*********************************************')

# Apresente:
#     os novos nomes das colunas de dfDados
#     os 5 primeiros elementos de dfDados e  
#     um gráfico de linha de cada coluna dos 5 primeiras empresa
#     Usar  dfLucro.T (transposta)'


print('\n2A) Colunas de dfDados')
print(dfDados.columns.values)

print('\n2B)5 primeiros elementos de dfDados sem valores ausentes *')
semAusente = dfDados.notnull().index
print(dfDados.loc[semAusente].head(5))

print('\n2C) Gráfico de linha com o lucro por ano de cada empresa *')
dfLucro.head(5).T.drop('MaiorLucro').plot.line(title='lucro por ano de cada empresa')
plt.show()

#======================================================================
print('\n=========================================================')
#Questao3:
# Responda as seguintes perguntas:
 
print('\n3a)Quantas pessoas trabalham em cada área?')
print(dfDados.AreaAtividade.value_counts())

print('\n3b)Qual a soma do LUCRO das empresas com mais de 10 anos de fundação?')
anoAtual = 2023 # dependera do ano corrente
anoEmpresas10 = dfDados.loc[(anoAtual - dfDados.AnoDeCriacao) > 10]
print(dfLucro.loc[anoEmpresas10.index].sum().sum())

print('\n3c)Qual o ano de fundação das empresas com situação IRREGULAR?')
dfEmpIrre = dfSit.loc[dfSit.values == 'IRREGULAR']
print(dfDados.AnoDeCriacao.loc[dfEmpIrre.index])

print('\n3d) Número de filiais mín, máx, mediano e médio por area de ativ/situação? * oq deve ser agrupado')
dfAtivSitu = dfDados.groupby([dfDados['AreaAtividade'],dfSit['SITFISC']])
print(dfAtivSitu.agg(['min','max','median','mean']).NumeroDeUnidades)

print('\n3e)Qual(is) empresa(s) paga(m) pior?')
piorPagamento = dfDados.SalarioMedio.min(axis=0)
empPagamPior =  dfDados.loc[dfDados.SalarioMedio == piorPagamento]
print(empPagamPior)
     
#======================================================================
print('\n=========================================================')

#Questao4:
# Criando categorias:
   
#    dfDados:
#     - Categorize a existência da empresa levando em consideração
#       o ano de fundação nas seguintes faixas:
#              0  a  1999 (inclusive) - ANTIGA,
#              a partir de 1999 até 2010 (inclusive) - NORMAL,
#              acima de 2010 - JOVEM,

#    dfLucro:
#     - Considerendo a coluna LUCRO, categorize a lucratividade das
#       empresas em 3 faixas de mesma amplitude identificando as faixas
#       como POUCO,MEDIO,MUITO'
   
# Mostre as tabelas de frequências resultante do cruzamento de:
#              existência x lucratividade  
#              área de atividade X existência,lucratividade
# Mostre o salário médio por lucratividade X área de atividade,existência

srCatAnoFunda = pd.cut(dfDados.AnoDeCriacao,bins=[0,1999,2010,dfDados.AnoDeCriacao.max()],labels=['ANTIGA','NORMAL','JOVEM'])

srCatLucro = pd.cut(dfLucro.MaiorLucro,bins=3,labels=['POUCO','MEDIO','MUITO'])

crFundaLucro = pd.crosstab(srCatAnoFunda,srCatLucro)

crAreaAtiFundaLucro = pd.crosstab(dfDados.AreaAtividade,[srCatAnoFunda,srCatLucro])

print('\n4A -Tabela de frequência existência x lucratividade')
print(crFundaLucro)
 
print('\n4B -Tabela de frequência área de atividade X existência,lucratividade')
print(crAreaAtiFundaLucro)

print('\n4C -Salário médio por lucratividade X área de atividade,existência')  
crSalLucAtiExi = pd.crosstab(srCatLucro,[dfDados.AreaAtividade,srCatAnoFunda],dfDados.SalarioMedio,aggfunc='mean')
print(crSalLucAtiExi)
#======================================================================
print('\n=================FIM  =============================')