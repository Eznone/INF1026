#GRUPO 1 - GABARITO DO TRABALHO DE INF1026

#Meus dados: 
#Enzo Mediano, 2211731, 33C

#Integrantes: 
#Alana da Silva Cabral, Drika Gonçalves Flinte,
#Enzo Tres Mediano, Rafael Ayres de Castro

#TEMA / BANCO DE DADOS:  Ranking de universidades

import pandas as pd
import matplotlib.pyplot as plt

dfRanking = pd.read_excel('ranking.xlsx',index_col=0,header=0)

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


print('------------------------------------------------------')
print('1.b- Coluna Female Ratio preenchida')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('1.c- Coluna Male Ratio preenchida')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('1.d- Coluna Citations Score preenchida')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('1.e- Coluna Location alterada')
print('------------------------------------------------------')


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


print('------------------------------------------------------')
print('2.b- Universidades sem país')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('2.c- Total de alunos')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('2.d- Percentual de pontuação de ensino maior que 70')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('2.e- Universidades com pontuação de pesquisa e citações maior que 85')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('2.f- Colocações da universidades dos USA')
print('------------------------------------------------------')


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


print('------------------------------------------------------')
print('3.b- Gráfico da tabela de frequência percentual das faixas SITFUN')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('3.c- Exiba a coluna TAMANHO (categoria de tamanho)')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('3.d- Tabela de frequência de categoria de tamanho X países')
print('------------------------------------------------------')


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


print('------------------------------------------------------')
print('4.b- Gráfico da tabela de frequência das universidades por países')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.c- Universidade com maior presença feminina')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.d- Universidades com menor presença internacional')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.e- Nota geral média, mínima e máxima por país x categoria de funcionários')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.f- Porcentagem média por Universidade X Estudantes internacionais')
print('------------------------------------------------------')


print('4.g- Porcentagem média por País X Porcentagem de estudante feminina')
print('------------------------------------------------------')


print('------------------------------------------------------')
print('4.h- Nota de pesquisa média por país x categoria de tamanho')
print('------------------------------------------------------')

