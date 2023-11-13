#GRUPO 1 - GABARITO DO TRABALHO DE INF1026

#Meus dados:
#Enzo Mediano, 2211731, 33C

#Integrantes: 
#Alana da Silva Cabral, Drika Gonçalves Flinte,
#Enzo Tres Mediano, Rafael Ayres de Castro

#TEMA / BANCO DE DADOS:  Ranking de universidades


import pandas as pd
import matplotlib.pyplot as plt

import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'ranking.xlsx'
path = os.path.join(pre, fname)

dfRanking = pd.read_excel(path,index_col=0,header=0)
pd.set_option('display.max_columns', None)


'''
O arquivo ranking.xlsx armazena os dados das 250 melhores universidades do mundo em 2023.

Uma empresa de ensino, deseja conhecer dados sobre as melhore universidade do mundo
em 2023 e, para isso, fizerem um ranking selecionando 250 instituições de ensino 
superior. Para conhecer melhor o perfil de cada faculdade, a empresa obteve os seguintes
dados: 
    o	Name of University: nome da instituição de ensino;
    o	Location: país onde a universidade esta localizada;
    o	Number of student: total de estudantes na universidade;
    o	No of student per staff: quantidade de funcionários da universidade por estudantes; 
    o	International Student: porcentagem de estudantes internacionais;
    o	Female Ratio: proporção de estudantes de sexo feminino;
    o	Male Ratio: proporção de estudantes de sexo masculino;
    o	OverAll Score: pontuação geral da universidade; 
    o	Teaching Score: pontuação de ensino;
    o	Research Score: pontuação de pesquisas;
    o	Citations Score: pontuação de citações; 
    o	Industry Income Score:pontuação de renda da indústria;
    o	International Outlook Score: Pontuação de perspectiva internacional; 
      
'''

#======================================================================
# 1- Consertando dfRanking:
# Nos itens a, b, c, d, após a operação, exiba os 6 primeiros registros:
#       a- Altere o nome das colunas para que fiquem no máximo
#          com 6 letras, sem espaços e em maiúsculas
#       b- Substitua valores ausentes na coluna Female Ratio pela média  
#          (numero inteiro) de estudantes de sexo feminino 
#       c- Substitua valores ausentes na coluna Male Ratio pela media
#          (numero inteiro) de estudantes do sexo masculino por Location 
#       d- Substitua valores ausentes na coluna Citations Score por 0
#       e- Substitua os valores United States por USA e os valores United 
#          Kingdom por UK
#======================================================================

print('------------------------------------------------------')
print('1.a- Nomes das colunas alterados')
print('------------------------------------------------------')
dfRanking.rename(columns = {"University Rank" : "UNRANK", "Name of University" : "UNNAME", "Location" : "LOC", "Number of student" : "NUMSTU", "No of student per staff" : "FUNEST", "International Student" : "INTSTU", "Female Ratio" : "FEMRAT", "Male Ratio" : "MALRAT", "OverAll Score" : "ALLSCO", "Teaching Score": "TEASCO", "Research Score": "RESSCO", "Citations Score" : "CITSCO", "Industry Income Score" : "INCSCO", "International Outlook Score" : "OUTSCO"}, inplace = True)
print(dfRanking.head(6))

print('------------------------------------------------------')
print('1.b- Coluna Female Ratio preenchida')
print('------------------------------------------------------')
dfRanking.FEMRAT.fillna(dfRanking.FEMRAT.mean(), inplace = True)
print(dfRanking.head(6))
#Para ver o fillna funcionando remove o comentario da proxima linha
#print(dfRanking.tail(6))

print('------------------------------------------------------')
print('1.c- Coluna Male Ratio preenchida')
print('------------------------------------------------------')
agLoc= dfRanking.groupby('LOC')
dfRanking.fillna(value= {'MALRAT':agLoc['MALRAT'].transform("mean")},inplace=True)
print(dfRanking.head(6))
#Para ver o fillna funcionando remove o comentario da proxima linha
#print(dfRanking.tail(6))

print('------------------------------------------------------')
print('1.d- Coluna Citations Score preenchida')
print('------------------------------------------------------')
dfRanking.CITSCO.fillna(0, inplace = True)
print(dfRanking.head(6))

print('------------------------------------------------------')
print('1.e- Coluna Location alterada')
print('------------------------------------------------------')
dfRanking.LOC.replace({"United States" : "USA", "United Kingdom" : "UK"}, inplace = True)
print(dfRanking.head(6))

#======================================================================
# 2- Conhecendo o dfRanking:
#       a- Exiba as informações da estrutura do DataFrame
#       b- Mostre os nomes das universidades que estão com país ausente
#       c- Soma dos alunos que estudam nas 250 melhores universidades do
#          mundo em 2023
#       d- Mostre o percentual de universidades com pontuação de ensino 
#          maior do que 70
#       e- Mostre o nome das universidades que tenham pontuação de pesquisa
#          e pontuação de citações maior que 85
#       e- Exiba o df ordenado descrescentemente por pontuação de ensino
#       f- Mostre as colocações(índices) das universidades localizadas 
#          nos USA
#======================================================================

print('------------------------------------------------------')
print('2.a- Informações desse DataFrame')
print('------------------------------------------------------')
dfRanking.info()

print('------------------------------------------------------')
print('2.b- Universidades sem país')
print('------------------------------------------------------')
dfSemPais = dfRanking.loc[dfRanking.LOC.isnull()]
print(dfSemPais.head(6))

print('------------------------------------------------------')
print('2.c- Total de alunos')
print('------------------------------------------------------')
print(f"Total de estudantes: {dfRanking.NUMSTU.sum(axis = 0)}")

print('------------------------------------------------------')
print('2.d- Percentual de pontuação de ensino maior que 70')
print('------------------------------------------------------')
dfSimaDe70 = dfRanking.loc[dfRanking.ALLSCO > 70]
print(f"Percentual pontuacao maior que 70: {dfSimaDe70.size / dfRanking.size * 100}")

print('------------------------------------------------------')
print('2.e- Universidades com pontuação de pesquisa e citações maior que 85')
print('------------------------------------------------------')
dfSimaDe85 = dfRanking.loc[(dfRanking.RESSCO > 85) & (dfRanking.CITSCO > 85)]
print(f"Percentual pontuacao pesquise e citações maior que 85: {dfSimaDe85.size / dfRanking.size * 100}")

print('------------------------------------------------------')
print('2.f- Colocações da universidades dos USA')
print('------------------------------------------------------')
dfUSA = dfRanking.loc[dfRanking.LOC == "USA"]
dfUSA = dfUSA.UNNAME
print(dfUSA.head(6))

#======================================================================
# 3- Alterando o dfRanking: 
#       a- Inclua e exiba a coluna SITFUN considerando 4 faixas de mesma  
#          amplitude para a coluna 'FUNEST'sendo a 1ª denominada "POUQUISSIMOS", 
#          a 2ª denominada "POUCOS", a 3ª denominada "BOM" e a última, 
#          "EXCELENTE"
#       b- Apresente a visualização gráfica da tabela de frequência percentual
#          das faixas de situação da quantidade de funcionários
#       c- Inclua e exiba a coluna TAMANHO com a respectiva categoria de tamanho,
#          devem ser criadas 4 categorias de acordo com os seguintes critérios:
#                "PEQUENA": NUMEST < 10000
#                "MEDIA": 10000<=idade<20000
#                "GRANDE": 20000<=idade<30000
#                "ENORME": idade >= 70 
#       d- Apresente a tabela de frequência de categoria de tamanho das
#          universidades X países
#======================================================================


print('------------------------------------------------------')
print('3.a- Exiba a coluna SITFUN (categoria de funcionários)')
print('------------------------------------------------------')
dfRanking["SITFUN"] = pd.cut(dfRanking.FUNEST, bins = 4, labels = ["POUQUISSIMOS", "POUCOS", "BOM", "EXCELENTE"])
print(dfRanking.SITFUN.head(30))

print('------------------------------------------------------')
print('3.b- Gráfico da tabela de frequência percentual das faixas SITFUN')
print('------------------------------------------------------')
dfRanking.SITFUN.value_counts().plot.pie(title = "Tab Freq Percentual das faixas SITFUN", autopct = "%.1f")
plt.show()

print('------------------------------------------------------')
print('3.c- Exiba a coluna TAMANHO (categoria de tamanho)')
print('------------------------------------------------------')
dfRanking["TAMANHO"] = pd.cut(dfRanking.NUMSTU, bins = [0, 10000, 20000, 30000, dfRanking.NUMSTU.max()], labels = ["PEQUENA", "MEDIA", "GRANDE", "ENORME"])
print(dfRanking.TAMANHO.head(10))

print('------------------------------------------------------')
print('3.d- Tabela de frequência de categoria de tamanho X países')
print('------------------------------------------------------')
dfRankingCrossed = pd.crosstab(index = dfRanking.TAMANHO, columns = dfRanking.LOC)
print(dfRankingCrossed)

#======================================================================
# 4- Analisando o dfRanking:
#       a- Crie a dfPaises e remova as linhas com valores nulos da coluna
#          "PAIS"
#       b- Exiba graficamente(barras) uma tabela de frequência das 
#          universidades por países
#       c- Exiba as universidade com maior porcentagem de presença feminina
#       d- Exiba as universidade com menor porcentagem de alunos internacionais
#       e- Exiba a porcentagem média por Universidade X Estudantes internacionais
#       f- Exiba porcentagem média por País X Porcentagem de estudante feminina
#       g- Qual a nota geral média, mínima e máxima atribuida a universidades
#          por país x categoria de funcionários
#       h- Qual a nota de pesquisa média por país x categoria de tamanho
#======================================================================

print('------------------------------------------------------')
print('4.a- Exiba a dfPaises')
print('------------------------------------------------------')
dfPaises = dfRanking.dropna(subset = ["LOC"])
print(dfPaises.head(20))


print('------------------------------------------------------')
print('4.b- Gráfico da tabela de frequência das universidades por países')
universidades_por_pais = dfRanking['LOC'].value_counts()
universidades_por_pais.plot(kind='bar')
plt.title('Tabela de Frequência das Universidades por Países')
plt.xlabel('País')
plt.ylabel('Número de Universidades')
plt.show()
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.c- Universidade com maior presença feminina')
print('------------------------------------------------------')
dfMaxPresFem = dfRanking.loc[dfRanking.FEMRAT == dfRanking.FEMRAT.max()]
print(f"Universidades maior presenca feminina: {dfMaxPresFem}")

print('------------------------------------------------------')
print('4.d- Universidades com menor presença internacional')
print('------------------------------------------------------')
dfMenPresInt = dfRanking.loc[dfRanking.INTSTU == dfRanking.INTSTU.min()]
print(f"Universidades menor presenca internacional: {dfMenPresInt}")

print('------------------------------------------------------')
print('4.e- Porcentagem média por Universidade X Estudantes internacionais')
porcentagemMediaUNNAMExINTSTU = dfRanking.groupby('UNNAME')['INTSTU'].mean()
print(porcentagemMediaUNNAMExINTSTU)

print('------------------------------------------------------')
print('4.f- Porcentagem média por País X Porcentagem de estudante feminina')
porcentagemMediaLOCxFEMRAT = dfRanking.groupby('LOC')['FEMRAT'].mean()
print(porcentagemMediaLOCxFEMRAT)
print('------------------------------------------------------')

print('------------------------------------------------------')
print('4.g- Nota geral média, mínima e máxima por país x categoria de funcionários')
notaGeral= dfRanking.groupby(['LOC', 'SITFUN'])['ALLSCO'].agg(['mean', 'min', 'max'])
print(notaGeral)
print('------------------------------------------------------')

print('------------------------------------------------------')
print('4.h- Nota de pesquisa média por país x categoria de tamanho')
notaPesquisa = dfRanking.groupby(['LOC', 'TAMANHO'])['RESSCO'].mean()
print(notaPesquisa)
print('------------------------------------------------------')

