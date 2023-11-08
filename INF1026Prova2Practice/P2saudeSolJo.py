# -*- coding: latin-1 -*-
############################################################################################
#Nome completo:
#Matr�cula PUC-Rio:
#Declara��o de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                 sem consultas a outros alunos, professores ou qualquer outra pessoa.
##############################################################################1#############
import pandas as pd
import matplotlib.pyplot as plt
import random
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('=================================')
print('Trabalhando com PANDAS')
print('=================================')
'''
Uma empresa de planos de sa�de, deseja conhecer o perfil de seus clientes
e suas opini�es sobre o plano BASEMED e, para isso, selecionou alguns clientes.
Para conhecer o perfil dos clientes selecionados, obteve os seguintes dados 
cadastrais: estado, g�nero, estado civil, idade, escolaridade e rendimento 

Para saber a opini�o dos clientes selecionados, enviou o question�rio abaixo
para ser respondido. No entanto, nem todo cliente selecionado 
(com dados cadastrais) respondeu o question�rio;
AVALIA��O DO PLANO DE SA�DE BASEMED
D� uma nota entre 0 e 10 para as perguntas abaixo
1. Qu�o f�cil � encontrar perto da sua �rea de resid�ncia, um m�dico 
    que tenha acordo com o seu plano de sa�de? 
    (0 � nada f�cil a 10-extremamente f�cil)
2. Qu�o satisfeito est� com a nossa rede credenciada de m�dicos
    dispon�veis para o seu plano de sa�de? 
    (0 � nada satisfeito a 10-extremamente satisfeito)
3. Qu�o f�cil � submeter uma reclama��o dos nossos servi�os? 
    (0 � nada f�cil a 10-extremamente f�cil)
4. Qu�o r�pida � a resolu��o da sua reclama��o? 
    (0 � nada r�pida a 10-extremamente r�pido)
5. Quando submete uma reclama��o, qu�o satisfeito fica com a resolu��o da mesma?
    (0 � nada satisfeito a 10-extremamente satisfeito)
6. Qu�o amig�veis s�o os colaboradores m�dicos da nossa empresa? 
    (0 � nada amig�veis a 10-extremamente amig�veis)
7. Qu�o conhecedores s�o os colaboradores m�dicos da nossa empresa? 
    (0-nada conhecedores a 10 extremamente conhecedores)
8. Qu�o razo�veis s�o os pre�os praticados pela nossa empresa? 
    (0- nada razo�veis a 10 extremamente razo�veis)
9. De forma geral, qu�o satisfeito ou insatisfeito est� com o servi�o 
    prestado pela nossa empresa? 
    (0 � extremamente insatisfeito a 10 � extremamente satisfeito)
10. Qu�o prov�vel � a renova��o do seu plano de sa�de na nossa empresa? 
    (0 � nada prov�vel a 10 � extremamente prov�vel)

O arquivo pesquisaSaude21.xlsx armazena o perfil dos entrevistados, os resultados
da pesquisa, o texto das perguntas do question�rio sobre o plano de sa�de e 
respectivos pesos. H� 3 planilhas. Os entrevistados t�m como identificador o
nome, presente em todas as planilhas relativas aos clientes.

- A planilha perfil tem os seguintes dados cadastrais do cliente entrevistado:
  o  NOME: identifica��o do cliente
  o  UF: sigla do estado de origem do cliente
  o  ESTADO CIVIL: estado civil - valores: CASADO, DIVORCIADO, SOLTEIRO, OUTROS
  o  GENERO: valores: F, M ou X
  o  IDADE: em anos
  o  ESCOLARIDADE COMPLETA: valores: FUNDAMENTAL, MEDIO ou SUPERIOR.
  o  RENDIMENTO MENSAL:  rendimento mensal do cliente em quantidade de sal�rios

- A planilha planoSaude, al�m do NOME, armazena as respostas dos clientes
  a cada uma das perguntas do question�rio. As perguntas foram identificadas
  por Pxx, onde xx � o n�mero da pergunta no question�rio e as respostas s�o
  notas entre 0 e 10.
 Entretanto � importante salientar que nem todos os entrevistados responderam
 o question�rio.

- A planilha questionarioSaude armazena o question�rio aplicado, ou seja,
  o texto das perguntas e o peso de cada pergunta no c�lculo da nota final
  (m�dia ponderada).

Os seguintes DataFrames est�o disponibilizados:

- dfPerfil (da planilha perfil): descri�ao do perfil do cliente 
       �ndice: NOME
       colunas: UF,ESTADO CIVIL,GENERO,IDADE, ESCOLARIDADE COMPLETA, 
                RENDIMENTO MENSAL
        valores: dados cadastrais descritos acima

- dfRespostas (da planilha planoSaude): notas atribu�das �s perguntas pelos clientes
        �ndice: NOME  
        colunas: P01,P02,P03,P04,P05,P06,P07,P08,P09,P10 (identif. da pergunta)
        valores: nota atribu�da entre 0 e 10

- dfQuestoes (da planilha question�rioSaude): descri��o do question�rio
        �ndice: PO1 a P10 ( identifica��o da pergunta) 
        colunas: TEXTO: descri��o da pergunta
                 PESO: import�ncia da pergunta no c�lculo da Nota Final 
                 (m�dia ponderada)


'''
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'pesquisaSaude21.xlsx'
path = os.path.join(pre, fname)

dfPerfil=pd.read_excel(path,sheet_name='perfil',header=0,index_col=0)
dfRespostas=pd.read_excel(path,sheet_name='planoSaude',header=0,index_col=0)
dfQuestoes=pd.read_excel(path,sheet_name='questionarioSaude',header=0,index_col=0)
print('==============================================')

print('Quest�o 1 - (1.7 pontos)')
# 
#======================================================================
# 1- Consertando dfPerfil:
# Nos itens a, b, c, d, ap�s a opera��o, exiba os 6 primeiros registros:
# (0.2) a- Altere o nome das colunas para que fiquem no m�ximo
#          com 6 letras, sem espa�os e em mai�sculas
# (0.3) b- Elimine registros com valores ausentes na coluna UF. 
#          Caso voc� n�o saiba resolver, substitua os valores ausentes
#          da coluna UF por "XX", mas vc n�o ter� a pontua��o do item.
# (0.2) c- Substitua valores ausentes na coluna GENERO por "D"
# (0.4) d- Substitua valores ausentes na coluna IDADE pela idade m�dia
#           por ESTADO CIVIL
#          Caso voc� n�o saiba resolver, substitua os valores ausentes
#          da coluna IDADE por 99, mas vc n�o ter� a pontua��o do item.
# (0.3) e- Substitua valores ausentes na coluna RENDIMENTO pelo valor
#          m�dio de rendimento dos entrevistados
#          Caso voc� n�o saiba resolver, substitua os valores ausentes
#          da coluna RENDIMENTO por 0.5, mas vc n�o ter� a pontua��o do item.
# (0.3) f- Exiba os 6 primeiros e os 6 �ltimos, juntos, ordenados
#          crescentemente por UF/GENERO
#======================================================================
# 
print('------------------------------------------------------')
print('1.a- Nomes das colunas alterados')
print('------------------------------------------------------')


dfPerfil.rename( columns=  {'ESTADO CIVIL':'ESTCIV',
                           'ESCOLARIDADE COMPLETA': 'ESCOLA',
                           'RENDIMENTO MENSAL': 'RENDM'},
                inplace=True)
#print(dfPerfil.columns)
print(dfPerfil.head(6))

print('------------------------------------------------------')
print('1-b- Sem UF vazios')
print('------------------------------------------------------')
# #SOL1: filtro de nulos
# fnul= dfPerfil.UF.isnull()
# dfPerfil= dfPerfil[~fnul]
# print(dfPerfil.head(6))


# #SOL2 : filtro de nao nulos
# fnaonul= dfPerfil.UF.notnull()
# dfPerfil= dfPerfil[fnaonul]
# print(dfPerfil.head(6))

# Usando dropna com subset
dfPerfil.dropna(subset=['UF'],inplace=True)
print(dfPerfil.head(6))

print('------------------------------------------------------')
print('1.c- G�nero preenchido')
print('------------------------------------------------------')

dfPerfil.fillna(value={'GENERO':"D"}, inplace=True)
print(dfPerfil.head(6))

print('------------------------------------------------------')
print('1.d- Idade preenchida')
print('------------------------------------------------------')

agEstCiv= dfPerfil.groupby('ESTCIV')
dfPerfil.fillna(value= {'IDADE':agEstCiv['IDADE'].transform(min)},
                inplace=True)
print(dfPerfil.head(6))


print('------------------------------------------------------')
print('1.e- Rendimento preenchido')
print('------------------------------------------------------')
dfPerfil.fillna(value= {'RENDM':dfPerfil.RENDM.mean()},
                inplace=True)
print(dfPerfil.head(6))


print('------------------------------------------------------')
print('1.f- Primeiros e �ltimos, juntos, ordenados por UF/GENERO')
print('------------------------------------------------------')
dfPrimUlt= dfPerfil.head(6).append(dfPerfil.tail(6))
print(dfPrimUlt.sort_values(['UF','GENERO']))


print('==============================================')

print('Quest�o 2 - (1.0 pontos)')
# 
#======================================================================
# 2- Alterando o dfPerfil: 
#   (0.5) a - Considere 4 faixas de mesma amplitude para a coluna RENDIMENTO
#             sendo a 1� denominada "D", a 2� denominada "C", a 3�
#              denominada "B" e a �ltima, "A":
#             - Substitua os valores de RENDIMENTO pela respectiva faixa
#             - Apresente a visualiza��o gr�fica da tabela de frequ�ncia
#               percentual das faixas de rendimento dos entrevistados
#
#   (0.5) b - Inclua a coluna CATID com a respectiva categoria de idade
#             Devem ser criadas 4 categorias de acordo com os seguintes
#             crit�rios:
#                "JOVEM": idade <30
#                "ADULTO": 30<=idade<50 
#                "SENIOR": 50<=idade<70
#                "AVANCADO": idade >= 70 
#            Apresente a tabela de frequ�ncia de categoria de idade x UF.
#======================================================================
# 
print('------------------------------------------------------')
print('2.a- Gr�fico da tabela de frequ�ncia percentual das faixas de rendimento')
print('------------------------------------------------------')

dfPerfil['RENDM']= pd.cut(dfPerfil['RENDM'],  bins=4,
                          labels=['D','C','B','A'])

#print(dfPerfil.head(6)) # para verificacao
srTabFreqRend= dfPerfil['RENDM'].value_counts()
srTabFreqRend.plot.pie(title='Tab Freq de Rendimentos', autopct='%.1f')
plt.show()


print('------------------------------------------------------')
print('2.b- Tabela de frequ�ncia de categoria de idade x UF')
print('------------------------------------------------------')
dfPerfil['CATID']= pd.cut(dfPerfil['IDADE'],  
                          bins=[0,29,49,69,dfPerfil['IDADE'].max()],
                          labels=['JOVEM','ADULTO','SENIOR','AVANCADO'])

#print(dfPerfil.head(6)) # para verificacao
ctCatIdxUF= pd.crosstab(index=dfPerfil['UF'] , columns=dfPerfil['CATID'])
print(ctCatIdxUF)

print('==============================================')

print('Quest�o 3 - (0.9 pontos)')
# 
#======================================================================
# 3- Conhecendo os clientes selecionados:
#    Exiba: 
#    (0.2) a- o percentual de entrevistados de cada g�nero 
#    (0.2) b- em um gr�fico de barras, as idades dos entrevistados que 
#             n�o s�o do RJ
#    (0.3) c- sem repeti��o, as UFs dos entrevistados com escolaridade
#             "SUPERIOR" que tamb�m responderam a pesquisa, ou seja, 
#             est�o no dfRespostas
#    (0.2) d- o menor valor e a mediana das idades para cada g�nero
#======================================================================
# 
print('------------------------------------------------------')
print('3.a- Percentual de entrevistados por g�nero')
print('------------------------------------------------------')
srPercGen= dfPerfil['GENERO'].value_counts(normalize=True)
print(srPercGen*100)  # opcional *100

print('------------------------------------------------------')
print('3.b- Gr�fico de Barras das idades dos que n�o s�o de RJ')
print('------------------------------------------------------')
srBoolNaoRio= dfPerfil.UF!= 'RJ' 
dfNaoRio= dfPerfil.loc[srBoolNaoRio]
#print(dfNaoRio) # para verificacao
dfNaoRio['IDADE'].plot.bar(title='Idades fora do RJ')
plt.show()


print('------------------------------------------------------')
print('3.c- UF sem repeti��o dos clientes com escolaridade SUPERIOR com resposta')
print('------------------------------------------------------')
dfNosDois= pd.concat([dfPerfil, dfRespostas], axis=1, join='inner')
#print(dfNosDois) # para verificacao
fesc= dfNosDois['ESCOLA']=='SUPERIOR'
print(dfNosDois.loc[fesc]['UF'].unique())

print('------------------------------------------------------')
print('3.d- Sumariza��es por g�nero')
print('------------------------------------------------------')
print(dfPerfil.groupby('GENERO')['IDADE'].agg(['min','median']))


print('==============================================')

print('Quest�o 4 - (0.9 pontos)')
# 
#======================================================================
# 4- Consertando e conhecendo o dfRespostas
#   (0.3) a- Elimine os entrevistados que foram exclu�dos do dfPerfil.
#            Exiba os 5 primeiros do dfRespostas
# 
#   (0.3) b- Mostre para cada pergunta do dfRespostas, o texto da pergunta e
#            a nota m�dia da pergunta considerando todos os entrevistados.
# 
#   (0.3) c- Quantos entrevistados consideram que: 
#           os pre�os praticados s�o pouco ou nada razo�veis (nota de P08 <=5)
#           E
#           � moderadamente prov�vel que renovar�o o plano de Sa�de
#                         (nota de P10 entre 5 e 7)? 
#======================================================================
# 
print('------------------------------------------------------')
print('4.a- dfRespostas com mesmos elementos que dfPerfil')
print('------------------------------------------------------')
dfRespostas= dfRespostas.loc[dfRespostas.index.isin(dfPerfil.index)]
print(dfRespostas.head(5))

print('------------------------------------------------------')
print('4.b- Nota m�dia por quest�o')
print('------------------------------------------------------')
# # Para conhecer o texto das perguntas sera necessario usar o dfQuestoes
# print('\n--->')
# print(dfQuestoes) # para verificacao
# print('\n--->')
# print(dfRespostas)
srNtMedPorPerg= dfRespostas.mean()  # e� uma series
srNtMedPorPerg.name= 'NotaMediaPergunta'
# print('\n--->')
# print(srNtMedPorPerg ) # para verificacao
#concatenacao de series
resp= pd.concat([dfQuestoes.TEXTO,srNtMedPorPerg ], axis=1)
print('\n--->')
print(resp)


print('------------------------------------------------------')
print('4.c- Quantidade de entrevistados com  P08<=5 e P10 entre 5 e 7')
print('------------------------------------------------------')
sbool08e10= (dfRespostas.P08<=5)&(dfRespostas.P10>5)&(dfRespostas.P10<7)
print(sbool08e10.sum())


print('==============================================')

print('Quest�o 5 - (1.5 pontos)')
# 
#======================================================================
# 5- Analisando a pesquisa
#   (0.3) a- Construa a series srNotaGeral, com a nota geral dada
#            ao plano de sa�de por cada entrevistado.
#         A nota geral � a m�dia ponderada da nota atribu�da � pergunta
#         ao peso da pergunta: 
#            NotaGeral=(notaP01*pesoP01+ ...+notaP10*pesoP10)/soma(pesos)
#         Exiba os 5 primeiros elementos da Series
# 
#   (0.3) b- Crie o DataFrame dfCompleto, concatenando apropriadamente
#            dfPerfil,a coluna P10 do dfRespostas (Qu�o prov�vel � a 
#            renova��o do seu plano de sa�de na nossa empresa) e a
#            Series srNotaGeral.
#            Todos os clientes que constam no dfPerfil devem estar no
#            dfCompleto. Valores ausentes num�ricos devem ser substitu�dos
#            por 0 e categ�ricos por "NC"
#         Exiba os 5 primeiros do dfCompleto
# 
#   (0.9)c- Responda as seguintes perguntas no dfCompleto:
#           1- Qual a nota m�dia, mediana, m�nima e m�xima da P10
#              atribu�da pelos clientes do RJ por CATID X RENDIMENTO?
#
#           2- Mostre o gr�fico de dispers�o entre as notas da pergunta
#              P10 e a idade
#          
#           3- A nota geral m�dia por CATID x GENERO
#======================================================================
# 
print('------------------------------------------------------')
print('5.a- Primeiros elementos da series srNotaGeral')
print('------------------------------------------------------')

pesosPerg= dfQuestoes.PESO
totPesos= pesosPerg.sum()
# print(pesosPerg) # para verificacao
# # Sera�feita a multiplicacao de cada linha do dfRespostas pela 
# # series de peso: VER  df.mul(series) em operacoes aritmeticas


dfRespMul= dfRespostas.mul(pesosPerg)
print(dfRespMul)
srNotaGeral= dfRespMul.sum(axis=1)/totPesos
srNotaGeral.name= 'NotaGeral'
print(srNotaGeral.head(5))

print('------------------------------------------------------')
print('5.b- Primeiros elementos do dfCompleto')
print('------------------------------------------------------')
dfCompleto = pd.concat([dfPerfil,dfRespostas['P10'],srNotaGeral],axis=1) 
#  Lembrando que o join default e� outer
#  Se quisermos apenas os clientes que estao em dfPerfil
#  dfCompleto.loc[dfCompleto.index.isin(dfPerfil.index)] 

# print(dfCompleto) # para verificacao

dfCompleto[['P10','NotaGeral']]=dfCompleto[['P10','NotaGeral']].fillna(0)
print('\n')
print(dfCompleto.head(5))


print('------------------------------------------------------')
print('5.c.1- Sumariza��es por CATID x RENDIMENTO')
print('------------------------------------------------------')
dfRJ= dfCompleto.loc[dfCompleto.UF=='RJ']
print( dfRJ.groupby(['CATID','RENDM'])['P10'].agg(['mean', 'median', 'min', 'max']))
      
print('------------------------------------------------------')
print('5.c.2- Gr�fico de dispers�o de P10 e IDADE')
print('------------------------------------------------------')
dfCompleto.plot.scatter(x='IDADE', y= 'P10')
plt.show()

print('------------------------------------------------------')
print('5.c.3- A nota geral m�dia por CATID x GENERO')
print('------------------------------------------------------')
agCIdGen= dfCompleto.groupby(['CATID','GENERO'])
print(agCIdGen['NotaGeral'].mean())

print('\n')
#Usando crosstab
ctGenCatId= pd.crosstab(index= dfCompleto.GENERO, columns=dfCompleto.CATID,
                values=dfCompleto.NotaGeral, aggfunc='mean')
print(ctGenCatId)


