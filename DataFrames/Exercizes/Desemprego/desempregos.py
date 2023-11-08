"""
Considere as informaÃ§Ãµes de uma agencia que busca empregos para pessoas desempregadas.
As informaÃ§Ãµes encontram-se no arquivo desempregados.xlsx.
As pessoas inscritas nessa agÃªncia sÃ£o identificadas pelo nÃºmero de inscriÃ§Ã£o (inscriÃ§Ã£o).
Na planilha situaÃ§Ã£o encontram-se as seguintes informaÃ§Ãµes:
ï‚· AREA_DE_ATUACAO: Ã¡rea de trabalho de atuaÃ§Ã£o do inscrito
ï‚· ULT _SAL_EM_QTD_SAL_MINIMOS: valor do Ãºltimo salÃ¡rio recebido pelo inscrito em
seu Ãºltimo emprego, expresso em quantidade de salÃ¡rio mÃ­nimos da ocasiÃ£o
ï‚· MESES_DE_DESEMPREGO: tempo que o inscrito encontra-se desempregado, em
meses.
Na planilha dadospessoais encontram-se as informaÃ§Ãµes:
ï‚· ESTADO_CIVIL
ï‚· ESCOLARIDADE (Grau de instruÃ§Ã£o)
ï‚· SEXO
ï‚· IDADE
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'desempregados.xlsx'
path = os.path.join(pre, fname)

print('\n------------------------------------------------')
print('******************  PARTE 1 ********************')
print('------------------------------------------------')
print('1.1) Crie e exiba o dataframe dfSit com os dados da primeira planilha')
dfSit = pd.read_excel(path, sheet_name = "situacao", index_col = 0, header = 0)
print(dfSit)

print('\n------------------------------------------------')    
print('1.2) Renomeie as colunas para AREA, ULT_SAL, TEMPO. Exiba')
dfSit.rename(columns = {"AREA_DE_ATUACAO" : "AREA", "ULT _SAL_EM_QTD_SAL_MINIMOS" : "ULT", "MESES_DE_DESEMPREGO" : "TEMPO"}, inplace = True)
print(dfSit)

print('\n------------------------------------------------')
print('1.3) Crie e exiba o dataframe dfPessoal com os dados da segunda planilha.')
dfPessoal = pd.read_excel(path, sheet_name = "dadospessoais", index_col = 0, header = 0)
print(dfPessoal)

print('\n------------------------------------------------')    
print('1.4) Substitua os valores ausentes : Em ESTADO_CIVIL pela moda e em SEXO por "G" . Exiba.')
modacv= dfPessoal.ESTADO_CIVIL.mode().loc[0]
#print(modacv)
dfPessoal.fillna({"ESTADO_CIVIL" : modacv, "SEXO" : "G"}, inplace = True)
print(dfPessoal) 

print('\n------------------------------------------------')     
print('1.5) Crie o dataframe dfDados, juntando adequadamente os 2 DFs')
dfDados = pd.concat([dfSit, dfPessoal], axis = 1, join = "inner")
print(dfDados) 

print('\n------------------------------------------------')
print('******************  PARTE 2 ********************')
print('------------------------------------------------')
print('2.1) Qual a AREA (DE ATUACAO) com maior nÃºmero de desempregados? \
E qual Ã© esse nÃºmero?')
srTabFreqArea = dfDados.AREA.value_counts()
print(f"{srTabFreqArea.idxmax()} - {srTabFreqArea.max()}")

    
print('\n------------------------------------------------')    
print('2.2) Qual a quantidade de indivÃ­duos, o maior (Ãºltimo) salÃ¡rio, o menor salÃ¡rio \
e o salÃ¡rio mÃ©dio POR ESCOLARIDADE?')
agesc = dfDados.groupby("ESCOLARIDADE")
print(agesc.ULT.agg(["count","max", "min", "mean"]))
    
print('\n------------------------------------------------')     
print('2.3) Apresente a visualizaÃ§Ã£o grÃ¡fica da relaÃ§Ã£o idade X tempo de desemprego.')
dfDados.plot.scatter(x = "IDADE", y = "TEMPO")
plt.show()

print('\n------------------------------------------------')      
print('2.4) Apresente a visualizaÃ§Ã£o grÃ¡fica da relaÃ§Ã£o idade X Ãºltimo salÃ¡rio')
dfDados.plot.scatter(x = "IDADE", y = "ULT")
plt.show()  

print('\n------------------------------------------------')      
print('2.5) Apresente a visualizaÃ§Ã£o grÃ¡fica da relaÃ§Ã£o Ãºltimo salÃ¡rio X tempo de desemprego.')
dfDados.plot.scatter(x = "ULT", y = "TEMPO")
plt.show() 

print('\n------------------------------------------------')  
print('2.6) POR AREA (DE ATUAÃ‡ÃƒO), apresente: \
quantidade de indivÃ­duos, tempo mÃ©dio de desemprego, Ãºltimo salÃ¡rio mÃ©dio.')
agArea = dfDados.groupby("AREA")
p1 = agArea.TEMPO.agg(["count", "mean"])
p2 = agArea.ULT.agg(["mean"])
p2.rename(columns = {"mean" : "ULT_MEDIO"}, inplace = True)
dfresp = pd.concat([p1, p2], axis = 1)
dfresp.rename(columns = {"count" : "QUANT", "mean" : "TEMPO_MEDIO"}, inplace = True)
print(dfresp)

print('\n------------------------------------------------')  
print('2.7) Qual AREA DE ATUACAO teve o maior Ãºltimo salÃ¡rio mÃ©dio?')
print(f"{dfresp.ULT_MEDIO.idxmax()} - {dfresp.ULT_MEDIO.max()}")


print('\n------------------------------------------------')      
print('2.8) Obtenha e exiba a relaÃ§Ã£o das variÃ¡veis: ESTADO_CIVIL e ESCOLARIDADE')
civ_esc= pd.crosstab(index=dfDados.ESTADO_CIVIL,columns=dfDados.ESCOLARIDADE) 
print(civ_esc)

print('\n------------------------------------------------')  
print('2.9) Crie as seguintes categorias de idade: de “0 a 30”, de “31 a 45” e de “46 em diante”. Exiba.')
srFxEt = pd.cut(dfDados.IDADE, bins = [0, 30, 45, dfDados.IDADE.max()])
print(srFxEt)

print('\n------------------------------------------------')      
print('2.10) Obtenha e exiba a relaÃ§Ã£o das variÃ¡veis: ESCOLARIDADE e categoria de idade')
esc_fx = pd.crosstab(index = dfDados.ESCOLARIDADE, columns = srFxEt)
print(esc_fx)
    
print('\n------------------------------------------------')      
print('2.11) Apresente a tabela de frequÃªncia das categorias de idade')
srTabFreqDasFxEt = srFxEt.value_counts(ascending = True)
print(srTabFreqDasFxEt)
    

print('\n------------------------------------------------')      
print('2.12) Apresente a tabela de frequÃªncia percentual (relativa) das categorias de idade')
srTabFreqPerc = (srTabFreqDasFxEt * 100 / srTabFreqDasFxEt.sum())
print(srTabFreqPerc)

print('\n------------------------------------------------')      
print('2.13) Qual a quantidade de indivÃ­duos do sexo F por categoria de idade?')
sexoPotCat = pd.crosstab(index = dfDados.SEXO, columns = srFxEt)

print('\n------------------------------------------------')  
print('2.14) Visualize graficamente a tabela de frequÃªncia de AREA DE ATUACAO, de duas formas:\
barras e pizza.')
#use srTabFreqArea criada no item 2.1
srTabFreqArea.plot.bar(title = "Tab de Freq Area de Atuacao")
plt.show()
srTabFreqArea.plot.pie(title = "Tab de Freq Area de Atuacao", autopct = "%.1f")
plt.show()