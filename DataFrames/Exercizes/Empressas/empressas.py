import pandas as pd
import matplotlib.pyplot as plt

import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'cadastroempresas2020.xlsx'
path = os.path.join(pre, fname)

pd.set_option("display.max_rows",200)
pd.set_option("display.max_columns",100)

'''
O arquivo cadastroempresas2020.xlsx armazena informaÃ§Ãµes de algumas empresas
nas seguintes planilhas:
    
A planilha dados:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    AreaAtividade: Ã¡rea de atuaÃ§Ã£o da empresa. Por exemplo, uma academia ou 
                   centro esportivo atua na Ã¡rea de ESPORTES
    NumeroDeUnidades: quantidade de filiais da empresa
    QtdDeFuncionarios: nÃºmero de funcionÃ¡rios considerando todas as filiais	
    SalarioMedio: salÃ¡rio mÃ©dio dos funcionÃ¡rios, medido em nÃºmero de 
                  salÃ¡rios mÃ­nimos
    AnoDeCriacao: ano de fundaÃ§Ã£o da empresa
    
A planilha desempenho:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    Lucro2017: faturamento lÃ­quido no ano de 2017, em mil reais
    Lucro2018: faturamento lÃ­quido no ano de 2018, em mil reais       
    Lucro2019: faturamento lÃ­quido no ano de 2019, em mil reais 
    
A planilha situaÃ§Ã£o
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente        
    SituacaoFiscal: situaÃ§Ã£o fiscal ( REGULAR ou IRREGULAR) no ano atual
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
#  1A) dfDados: Exiba o percentual de empresas com mais de 20 funcionÃ¡rios e 
#               que tenham atÃ© 10 filiais
#  1B) dfLucro: Exiba o percentual de valores ausentes
#  1C) dfSit:   Exiba os 4 Ãºltimos elementos ordenados por NomeDaEmpresa'
#  1D) dfDados: Exiba os 8 primeiros elementos ordenados por NumeroDeUnidades/QtdDeFuncionarios 
#  1E) dfLucro: Exiba o percentual de empresas cujo lucro em 2018 foi superior ao lucro de 2019 
#  1F) dfSit:   Exiba a situaÃ§Ã£o das empresas Fominha,KurtExames e VemSerFit

print('\n1A -dfDados: perc de empresas > 20 funcionarios e com ate  10 filiais ')
sMas20FuncMen10Fil = dfDados.loc[(dfDados.QtdDeFuncionarios > 20) & (dfDados.NumeroDeUnidades <= 10)]
#print(sMas20FuncMen10Fil)
print((sMas20FuncMen10Fil.size / dfDados.size ) * 100)

print('\n1B) dfLucro: Exiba o percentual de valores ausentes ')
sValAusentes = dfLucro.isnull().sum().sum()
print(sValAusentes)

print('\n1C) dfSit: Exiba os 4 Ãºltimos elementos ordenados por NomeDaEmpresa')
print(dfSit.tail(4).sort_index())

print('\n1D) dfDados: os 8 prim ordenados por NumeroDeUnidades/QtdDeFuncionarios ')
print(dfDados.head().sort_values(["NumeroDeUnidades", "QtdDeFuncionarios"]))

print('\n1E) dfLucro: percentual de empresas com lucro em 2018 > lucro de 2019  ')
empressasLucroMaior = dfLucro.loc[dfLucro.LUCRO2018 > dfLucro.LUCRO2019]
print((empressasLucroMaior.size / dfLucro.LUCRO2017.size) * 100)

print('\nExtra1: DF com as empresas')
print(empressasLucroMaior)

print('\nExtra2: So nome das empresas')
print(list(empressasLucroMaior.index))

print('\n1F) dfSit:   Exiba a situaÃ§Ã£o das empresas Fominha,KurtExames e VemSerFit')
dfNovoSit = dfSit.loc[["Fominha", "KurtExames", "VemSerFit"]]
print(dfNovoSit)

#======================================================================
print('\n=========================================================')


#Questao2:
#  Consertando os Dataframes :

# Consertando os Dataframes 
#      dfDados: valores ausentes na coluna NumeroDeUnidades devem ser 
#               substituÃ­dos pela mÃ©dia da coluna',
#      dfDados: valores ausentes na coluna SalarioMedio devem ser
#               substituÃ­dos pelo menor valor de empresas de mesma Ã¡rea
#               de atividade
#      dfDados: renomeie as colunas para que sejam identificadas por
#               rÃ³tulos com atÃ© 6 caracteres, todos maiÃºsculos',


# OBS: o numero de unidades deve ser um inteiro

print('\n*********************************************')
print('******************  Q2  ********************')
print('*********************************************')
print('\nNovo dfDados')
#print(dfDados)
print('\n*********************************************')

#      dfLucro: substitua os valores ausentes de cada empresa pelo lucro 
#               mediano da empresa,
#      dfLucro: inclua a coluna LUCRO com o maior lucro nos 3 anos 
#               de cada empresa


print('\nPreenchidos usando DF transposto')
#MELHOR FORMA: trabalhar com DF transposto

dfLucro.T.fillna(dfLucro.median(axis = 1), inplace = True)
print(dfLucro)

dfLucro["LUCRO"] = dfLucro.max(axis = 1)


print('\n*********************************************')


print('\n*********************************************')

# Apresente:
#     os novos nomes das colunas de dfDados 
#     os 5 primeiros elementos de dfDados e  
#     um grÃ¡fico de linha de cada coluna dos 5 primeiras empresa
#     Usar  dfLucro.T (transposta)'


print('\n2A) Colunas de dfDados')
print(list(dfDados.columns))

print('\n2B)5 primeiros elementos de dfDados sem valores ausentes')
dfDadosNoNa = dfDados.dropna()
print(dfDadosNoNa.head(5))

print('\n2C) GrÃ¡fico de linha com o lucro por ano de cada empresa') 
dfLucro.T.dropna().plot.line()
plt.show()

#======================================================================
print('\n=========================================================')
#Questao3:
# Responda as seguintes perguntas:

dfGeral= pd.concat([dfDados,dfLucro, dfSit],axis=1,join='inner') 

print('\n3a)Quantas pessoas trabalham em cada Ã¡rea?')
dfgrouped = dfGeral.groupby('AreaAtividade')
print(dfgrouped.QtdDeFuncionarios.sum())
#print(dfGeral.groupby('AreaAtividade')['QtdDeFuncionarios'].sum())

print('\n3b)Qual a soma do LUCRO das empresas com mais de 10 anos de fundaÃ§Ã£o?')
anoAtual = 2022 # dependera do ano corrente
dfGeral["LucroTotal"] = dfGeral.LUCRO2017 + dfGeral.LUCRO2018 + dfGeral.LUCRO2019
dfFundacao = dfGeral.loc[dfGeral.AnoDeCriacao < anoAtual - 10]
print(dfFundacao.LucroTotal)

print('\n3c)Qual o ano de fundaÃ§Ã£o das empresas com situaÃ§Ã£o IRREGULAR?')
dfIrregulares = dfGeral.loc[dfGeral.SITFISC == "IRREGULAR"]
print(dfIrregulares.AnoDeCriacao)

print('\n3d) NÃºmero de filiais mÃ­n, mÃ¡x, mediano e mÃ©dio por area de ativ/situaÃ§Ã£o?')
groupedGeral = dfGeral.groupby(["AreaAtividade", "SITFISC"])
print(groupedGeral.QtdDeFuncionarios.agg(["min", "max", "median", "mean"]))

print('\n3e)Qual(is) empresa(s) paga(m) pior?')
dfPiorPage = dfGeral.loc[dfGeral.SalarioMedio == dfGeral.SalarioMedio.min()]
print(list(dfPiorPage.index))

      
#======================================================================
print('\n=========================================================')

#Questao4:
# Criando categorias:
    
#    dfDados: 
#     - Categorize a existÃªncia da empresa levando em consideraÃ§Ã£o 
#       o ano de fundaÃ§Ã£o nas seguintes faixas:
#              0  a  1999 (inclusive) - ANTIGA,
#              a partir de 1999 atÃ© 2010 (inclusive) - NORMAL,
#              acima de 2010 - JOVEM,

#    dfLucro: 
#     - Considerendo a coluna LUCRO, categorize a lucratividade das 
#       empresas em 3 faixas de mesma amplitude identificando as faixas 
#       como POUCO,MEDIO,MUITO' 
    
# Mostre as tabelas de frequÃªncias resultante do cruzamento de: 
#              existÃªncia x lucratividade  
#              Ã¡rea de atividade X existÃªncia,lucratividade
# Mostre o salÃ¡rio mÃ©dio por lucratividade X Ã¡rea de atividade,existÃªncia

srCutAnoFunda = pd.cut(dfDados.AnoDeCriacao, bins = [0, 1999, 2010, dfDados.AnoDeCriacao.max()], labels = ["ANTIGA", "NORMAL", "JOVEM"])
print(srCutAnoFunda)
srCutLucro = pd.cut(dfLucro.LUCRO, bins = 3, labels = ["POUCO", "MEDIA", "MUITO"])
print(srCutLucro)

print('\n4A -Tabela de frequÃªncia existÃªncia x lucratividade') 
dfCrossedExLuc = pd.crosstab(index = srCutAnoFunda, columns = srCutLucro)
print(dfCrossedExLuc)
  
print('\n4B -Tabela de frequÃªncia Ã¡rea de atividade X existÃªncia,lucratividade') 
dfCrossedAdaExLuc = pd.crosstab(index = dfGeral.AreaAtividade, columns = [srCutAnoFunda, srCutLucro])
print(dfCrossedAdaExLuc)

print('\n4C -SalÃ¡rio mÃ©dio por lucratividade X Ã¡rea de atividade,existÃªncia')  
print(pd.crosstab(index= srCutLucro, columns=[dfDados.AreaAtividade, srCutAnoFunda],values= dfDados.SalarioMedio, aggfunc='mean'))

print('\nOutra forma')
aggg=dfDados.groupby([dfDados.AreaAtividade,srCutAnoFunda,srCutLucro])
print(aggg.SalarioMedio.mean())
#======================================================================
print('\n=================FIM  =============================') 
