import pandas as pd
import matplotlib.pyplot as plt

import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'corredoresplus.xlsx'
path = os.path.join(pre, fname)

print('\n1- DataFrame dfCorredores')
dfCorredores = pd.read_excel(path,index_col=0,header =0)
print(dfCorredores)

#renomeie o índice apenas como num
print('\n2-index renomeado')
dfCorredores.index.name = "num"
print(dfCorredores)

print('\n3- Nome do(s) vencedor(es) da corrida e melhor tempo')
melhorTempo = dfCorredores.corrida.min()
dfVenc = dfCorredores.loc[dfCorredores.corrida == melhorTempo]
print(dfVenc)
print(dfVenc.nome.values)
print(f"Melhor Tempo: {melhorTempo}")

print('\n4- Nomes dos corredores com melhor desempenho na corrida do que no melhor treino')
dfTreino = dfCorredores[["treino1", "treino2", "treino3"]]
print(dfTreino)

srtempoMelhorTreino = dfTreino.min(axis = 1) #Axis 1 is for verical axis
print(srtempoMelhorTreino)

print(dfTreino.loc[dfCorredores.corrida < srtempoMelhorTreino])

print('\n5-Dataframe so com os que tiveram desempenho na corrida pior ou igual a media dos treinos')
srMediaTreinos = dfTreino.mean(axis = 1)
dfDesemp = dfCorredores.loc[dfCorredores.corrida <= srMediaTreinos]
print(dfDesemp)

print('\n6-Nome dos corredores que tiveram a maior diferenca entre o seu melhor treino e a corrida')
print('(para mais ou para menos)')
difTreinoCorrida = abs(dfCorredores.corrida - dfTreino.min(axis = 1))
print(difTreinoCorrida)
dfMelhores = dfCorredores.loc[difTreinoCorrida == difTreinoCorrida.max()]
print(dfMelhores)

print('\n7-Grafico Media do treino X corrida')#inclua a coluna Media
dfCorredores["MdTreino"] = srMediaTreinos

print('\n8-Grafico Melhor treino X corrida') #inclua a coluna MelhorTreino
dfCorredores["MelhorTreino"] = srtempoMelhorTreino
dfCorredores.plot.scatter(x = "MelhorTreino", y = "corrida")

print('\n9-Grafico de barras de treinos e corridas')


#Considerando agora o resultado final das corridas em 2017 e 2016

fname = 'corridasantigas.xlsx'
path = os.path.join(pre, fname)

sCorrida17=pd.read_excel(path,sheet_name='corrida2017',
                         index_col=0, header=None).squeeze()
sCorrida17.name='corrida2017'
print('\nCorrida em 2017')
print(sCorrida17)

sCorrida16=pd.read_excel(path,sheet_name='corrida2016',index_col=0, header=None).squeeze()
sCorrida16.name='corrida2016'
print('\nCorrida em 2016')
print(sCorrida16)

sCorrida18= pd.Series(dfCorredores.corrida.values,index=dfCorredores.nome)
sCorrida18.name= 'corrida2018'
print(sCorrida18)

#Crie o dfCorridas concatenando as corridas de 2016, 2017 e 2018. Exiba
print('\n10- dfCorridas')
dfCorridas = pd.concat([sCorrida16, sCorrida17, sCorrida18], axis = 1, join = "inner")
print(dfCorridas)

#Trabalhando com o dfCorridas, crie e exiba uma series srDesemp informando se o 
# com o passar dos anos  o desempenho do o corredor melhorou, piorou ou 
# ficou indefinido. Exiba o desempenho dos corredores
print('\n11-Desempenho geral nas 3 corridas')
def analisis(l):
    if l.corrida2016 < l.corrida2017 and l.corrida2017 < l.corrida2018:
        return 'PIOROU'
    elif l.corrida2016 > l.corrida2017 and l.corrida2017 > l.corrida2018:
        return 'MELHOROU'
    else:
        return 'indefinido'


srDesempGeral = dfCorridas.apply(analisis, axis = 1)
print(srDesempGeral)

print('\n12-Exibir graficamente os resultados das 3 corridas')
dfCorridas.plot.bar(title = "Resultados", figsize = (8,6))
plt.show()

print('\n13-Exibir graficamente quantos melhoraram e quantos pioraram percentualmente')
srTabFreq = srDesempGeral.value_counts()
srTabFreq.plot.pie(title = "DesempGeral", autopct = "%.1f")
plt.show()

print('\n14-Exibir numericamente quantos melhoraram e quantos pioraram percentualmente')
srTabFreqPerc = (srDesempGeral.value_counts() * 100) / (srTabFreq.sum())
print(srTabFreqPerc)

################################################################
# dfInfo criado a partir da planilha info do arq 

fname = 'corredoresplus.xlsx'
path = os.path.join(pre, fname)

print('\n15- DataFrame dfInfo')
dfInfo = pd.read_excel(path, sheet_name='info',
                             index_col=0,header =0)
print(dfInfo)

print('\n16- Exiba a tabela de frequencia dos estados ')
srEstadoFreq = dfInfo.ESTADO.value_counts()
print(srEstadoFreq)

print('\n17- Exiba graficamente o percentual de corredores do RJ ')
sbool = dfInfo.ESTADO == "RJ"
sbool.replace({True : "DoRJ", False: "NaoDoRJ"}, inplace = True)
sbool.value_counts().plot.pie(title = "Percentual do Rio", autopct = "%.1f")
plt.show()

print('\n18- Exiba a tabela de frequencia no cruzamento EQUIPE/ESTADO')
print(pd.crosstab(index = dfInfo.EQUIPE, columns = dfInfo.ESTADO))

print('\n19- Exiba as idades min,max e a quantidade de anos da atividade media por EQUIPE/ESTADO')
agEE = dfInfo.groupby(["EQUIPE", "ESTADO"])
print(agEE.agg({'IDADE' : ["min", "max"], 'QtdAnosAtiv' : ["mean"]}))

# Necessario agora criar um df  juntando colunas de interesse de 2 DFs
print('\n20- Graficamente(dispersao): Relacao entre idade e tempo na corrida de 2018')
currentCorrida = pd.Series(dfCorredores.corrida.values, index = dfCorredores.nome)
currentCorrida.name = "currCorrida"
print(currentCorrida)
dfIdadeCorrida = pd.concat([dfInfo.IDADE, currentCorrida], axis = 1)
print(dfIdadeCorrida)

dfIdadeCorrida.plot.scatter(x = "IDADE",  y = "currCorrida")
plt.show()