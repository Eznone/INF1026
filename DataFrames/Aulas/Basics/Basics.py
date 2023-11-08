import pandas as pd
import matplotlib.pyplot as plt

dicGraus={ 'Grau1': {'LALA':5.5,'LELE':2.4,'LILI':3.7,'DUDU':7.9},
           'Grau2': {'LALA':9.5,'LELE':6.5,'LILI':6.4,'DUDU':9.1}
        }

print('\n-------AULA1---------')
dfGraus= pd.DataFrame(dicGraus)

print('\n----------1----------')
#Exibe o df
print(dfGraus)

print('\n----------2----------')
#Exibe os indices
print(dfGraus.index)
print('\nSó rotulos:')
print(dfGraus.index.values)
print(list(dfGraus.index))

print('\n----------3----------')
# Exibe as colunas
print(dfGraus.columns)
print('\nSó rotulos:')
print(dfGraus.columns.values)
print(list(dfGraus.columns))

print('\n----------4----------')
#Exibe os valores
print(dfGraus.values)


print('\n----------5----------')
#Exibe quantidade de valores
print(dfGraus.size)

print('\n----------6----------')
# Exibe numLinhas e numColunas
print(dfGraus.shape)

print('\n----------7----------')
#Exibe num linhas
print(dfGraus.shape[0])

print('\n----------8----------')
#Exibe num colunas
print(dfGraus.shape[1])

print('\n----------9----------')
#Exibe 2 prim elementos
print(dfGraus.head(2))

print('\n----------10---------')
#Exibe 2 ult elementos
print(dfGraus.tail(2))

print('\n----------11---------')
#Exibe as informacoes do df
dfGraus.info()

print('\n----------12---------')
#Resumos estatisticos das colunas numericas
print(dfGraus.describe())

######### Medidas (funcoes) e eixos #########
print('\n----------13---------')
print('\nMedia dos GRAUS') # => default: axis=0 ou axis='index'
print(dfGraus.mean())
print('\n')
print(dfGraus.mean(axis=0))
print('\n')
print(dfGraus.mean(axis='index'))

print('\n----------14---------')
print('\nMedia dos ALUNOS') # =>  axis=1 ou axis='columns'
print(dfGraus.mean(axis=1))
print('\n')
print(dfGraus.mean(axis='columns'))

######### Selecao de Elementos #########
print('\n----------15---------')
#Exibe dados da LELE
#Exibe dados de LELE e DUDU
print(dfGraus.loc['LELE'])
print(type(dfGraus.loc['LELE']))
# retorna uma series
print('\n')
print(dfGraus.loc[['LELE']])
print(type(dfGraus.loc[['LELE']]))
# retorna um DF
print('\n')
print(dfGraus.loc[['LELE','DUDU']])
print(type(dfGraus.loc[['LELE','DUDU']]))
# retorna um DF

print('\n----------16---------')
#Exibe coluna Grau1
#  retorna series
print(dfGraus['Grau1'])
print('\n')
# pode usar dfGraus.Grau1: retorna series
print(dfGraus.Grau1)
print('\n')    
#Exibe colunas Grau1 Grau2
# retorna DF
print(dfGraus[['Grau1','Grau2']])

print('\n----------17---------')
#Exibe o Grau1 da LELE
#Elemento (celula). Tambem para alteracao
print(dfGraus.loc['LELE','Grau1']) # usada tb para alterar

print('\n----------18---------')
print(dfGraus.loc['LELE']['Grau1'])
#Outras formas #CORRETO: dfGraus.loc['LELE'].loc['Grau1']
print(dfGraus['Grau1'].loc['LELE'])

print('\n----------19---------')
# O DF
print(dfGraus)

print('\n----------20---------')
# DF transposto, seus indices e suas colunas
print(dfGraus.T)
print('INDEX:', dfGraus.T.index)
print('COLUMNS:', dfGraus.T.columns)


dfGraus.T.loc['Grau1','LELE']=10   #Alteracao do valor de uma celula

print('\n----------21---------')
print(dfGraus.T)

print('\n----------22---------')
print(dfGraus)

###############  VISUALIZACAO ###############
print('\n---------23----------')
#VISUALIZACAO: Barras => Todos os Graus juntos em um grafico unico
dfGraus.plot.bar(title='GRAUS JUNTOS', figsize=(6,4))
plt.show()

#VISUALIZACAO: Barras => Graus Separados
dfGraus.plot.bar(title='GRAUS SEPARADOS', subplots=True, figsize=(6,6))
plt.show()

#Visualização: grafico de linha
dfGraus.T.plot.line(title='GRAUS', figsize=(6,4))
plt.show()
###############  INCLUSOES ###############
print('\n---------24----------')
#INCLUSAO DE NOVA LINHA
srVava=pd.Series([9.4, 7.8], index=['Grau1','Grau2'])
print(srVava)
#Incluindo uma linha correspondente ao Vava
dfGraus.loc['VAVA']= srVava # poderia usar diretamente [9.4, 7.8]
print(dfGraus)

dfGraus.loc['KUKA']=0
print(dfGraus)

dfGraus.loc['TETE']=[3.6,9]
print(dfGraus)

print('\n---------25----------')
#INCLUSAO DE NOVA COLUNA
dicGrau3= {'LALA':9.5,'LELE':5.5,'LILI':6.2,'VAVA':8.2,'DUDU':2.7}
#Inclusao da coluna Grau3=
dfGraus['Grau3']=pd.Series(dicGrau3) 
#dfGraus['Grau4']=[1,2,None,4,5,6,7]
print(dfGraus)



############## Descartando NaN #############
print('\n---------26----------')
#Exibir sem linhas com NaN
print('\nSem linhas com NaN')
print(dfGraus.dropna(axis='index'))
#Exibir sem colunas com NaN
print('\nSem colunas com NaN')
print(dfGraus.dropna(axis='columns'))



###############  Aplicacao de FUNCAO  ###############
print('\n---------27A----------')
#Maior nota
print('\nMaior Nota por grau')
print(dfGraus.max(axis='index')) #axis = index

print('\nUm aluno com a maior nota por Grau')
print(dfGraus.idxmax(axis='index'))

print('\nMaior nota e 1 aluno de maior nota por grau')
print(dfGraus.agg(['max','idxmax'], axis='index'))

print('\nMaior Nota por aluno')
print(dfGraus.max(axis='columns'))

print('\nPor aluno, um grau em que o aluno tenha tirado sua maior nota')
print(dfGraus.idxmax(axis='columns'))

print('\nMaior nota e 1 grau de maior nota por aluno')
print(dfGraus.agg(['max','idxmax'], axis='columns'))

print('\n---------27B----------')
print('\nAplicando uma funçao nossa')

#Escreva uma função que receba uma series e retorne 
# a qtd de valores acima de 7 da series
def qtdAcDe7(sqq):
    sbool = sqq>7
    return sbool.sum()

print('\nQuantidade de notas acima de 7 por GRAU')
print(dfGraus.apply(qtdAcDe7, axis='index'))

print('\nQuantidade de notas acima de 7 por ALUNO')
print(dfGraus.apply(qtdAcDe7, axis='columns'))

###########################################
print('\n---------28----------')
print('\ndfGraus ')
#Para ficar interessante vou alterar o grau1 da KUKA
dfGraus.loc['KUKA','Grau1']=None
print(dfGraus)

print('\nPreenchimento de valores ausentes com 999')
print(dfGraus.fillna(999))

print('\nPreenchimento de valores ausentes com 0 no Grau1 e 1 no Grau3')
print(dfGraus.fillna({'Grau1':0,'Grau3':1}))

print('\nPreencher NaN com a media dos graus')
print(dfGraus.fillna(dfGraus.mean()))

#Voltando ao valor original
dfGraus.loc['KUKA','Grau1']=0
###########################################
print('\n---------29----------')
print('\n---Ordenacao---')
print('\n Exiba o DF ordenado pelos alunos')
print(dfGraus.sort_index())

print('\n Exiba o DF ordenado decrescentemente pelos alunos')
print(dfGraus.sort_index(ascending=False))

print('\n Exiba o DF ordenado decrescentemente pelos nomes das colunas')
print(dfGraus.sort_index(ascending=False, axis='columns'))

print('\nExiba o DF ordenado pelo Grau1')
print(dfGraus.sort_values('Grau1'))

#Para ficar interessante
dfGraus.loc['LILI','Grau1']= 3.6
print('\nExiba o DF ordenado pelo Grau1 decrescentemente')
print(dfGraus.sort_values(by='Grau1', ascending=False))

#Grau1 empate Lili e Tete: desempatar pelo Grau2
print('\nExiba o DF ordenado dec pelo Grau1, desempatando pelo Grau2 ')
print(dfGraus.sort_values(by=['Grau1','Grau2'], ascending=False))


###########################################
print('\n---------30----------')
print('\n---- Filtro ----')
print('Notas acima de 5')
print(dfGraus>5)

print('\n Exiba os elementos com Grau1 acima de 5')
print(dfGraus.loc[dfGraus.Grau1>5])

print('\n Exiba os elementos com Grau1 e Grau3 acima de 5')
print(dfGraus.loc[ (dfGraus.Grau1>5)&(dfGraus.Grau3>5)])

print('\n Exiba os elementos com Grau2 maior do que o Grau1')
print(dfGraus.loc[ dfGraus.Grau2>dfGraus.Grau1 ])

###############################################
###############################################
print('\n---------31----------')
print('\n-- Um segundo DF--')
#Um segundo DataFrame
dicOutros= {'NENE':{ 'Grau1':7.6, 'Grau3':2.8},
            'BUBA':{'Grau2':5.0},
            'GIGI':{'Grau1':5.4,'Grau2':8.6 },
            'TATA':{ 'Grau1':5.4, 'Grau2':7.8, 'Grau3':8.1}}
dfOutro= pd.DataFrame(dicOutros)
print(dfOutro,'\n')
dfOutro= dfOutro.T
print(dfOutro,'\n')

print('\n---------32----------')
print('\nMais preenchimento de valores ausentes')
#PREENCHIMENTO DE VALORES AUSENTES => COPIAS
#Copia1: Preenchendo todos os NaN por 1
print('\nPreenchendo todos os NaN por 1')
print(dfOutro.fillna(value=1))

#Copia2: Preenchendo NaN pela media das colunas (dos graus)=>eixo index
print('\nPreenchendo  NaN pela media dos graus')
sMedGraus= dfOutro.mean(axis=0)
print('--')
print(sMedGraus)
print('--')
print(dfOutro.fillna(value=sMedGraus))

#Copia3: Preenchendo NaN pela media das linhas (notas de cada aluno)=>eixo columns
# ATENCAO: nao implementado. Assim so trabalhando com o DF Transposto
print('\n')
print('\nPreenchendo  NaN pela media dos alunos')
dft= dfOutro.T
print(dft.fillna(value=dft.mean()).T)

#Copia4: Preenchendo NaN =>Grau1: 0, Grau2: media do Grau2, Grau3:mediana do Grau3
print('\n')
print('\nPreenchendo NaN =>Grau1: 0, Grau2: media do Grau2, Grau3:mediana do Grau3')
print(dfOutro.fillna(value={'Grau1':0,'Grau2':dfOutro.Grau2.mean(),
                            'Grau3': dfOutro.Grau3.median()} ))


########### CONCATENACAO #############
print('\n---------33----------')
#JUNTANDO DataFrames => concatenacao: default axis=0 e join = 'outer'
#dfOutro com NaN
print('\n----------------')
print(dfGraus)
print('\n----------------')
print(dfOutro)
print('\n----------------')
print('\nConcatenação: default (axis=0), alinha pela coluna')
dfJuntos1= pd.concat([dfGraus, dfOutro])
print(dfJuntos1,'\n')


dic3={ 'EXTRA1': {'LELE':8.4, 'VAVA':8.8, 'DUDU': 8.9, 'MIMI':8.6},
        'EXTRA2': {'LELE':6.4, 'VAVA':7.8, 'DUDU': 6.9, 'MIMI':7.6}
      }

df3= pd.DataFrame(dic3)
print(df3,'\n')

#Outras concatenacoes: a default nao eh interessante
print('\nConcatenacao deualt nao interessante')
dfJuntos2= pd.concat([dfGraus,df3 ])
print(dfJuntos2,'\n')

print('\n****')
# axis=1, considerando TODOS os elementos join='outer' (join default)
#dfJuntos3= pd.concat([dfGraus,df3 ], axis=1,join = 'outer')
print('\nConcatenacao axis=1 (alinha pelos indices)')
dfJuntos3= pd.concat([dfGraus,df3 ], axis=1,join = 'outer')
print(dfJuntos3,'\n')

# axis=1, considerando somente os que tem todas as colunas join='inner' (intersecao)
print('\nConcatenacao axis=1 (alinha pelos indices), so indices em ambos DFs')
dfJuntos4= pd.concat([dfGraus,df3 ], axis=1,join = 'inner')
print(dfJuntos4,'\n')

print('\n---------34---------')
#Renomeando Colunas
print('\nRenomeando Colunas')
dfJuntos4.rename(columns={'Grau1':'G1','Grau2':'G2','Grau3':'G3'},inplace=True)
print(dfJuntos4)
