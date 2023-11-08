import pandas as pd
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'CelularGeral.xlsx'
path = os.path.join(pre, fname)

'''
1- Crie o dataframe dfCaracCel a partir da planilha caracteristicas do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas
'''

print('\n1-O dfCaracCel')
dfCaracCel = pd.read_excel(path, sheet_name='caracteristicas', header=0,index_col=0)
print(dfCaracCel)

print('\n2-Exiba as informacoes do dfCelular')
dfCaracCel.info()

print('\n3-Exiba a coluna fabricante')
print(dfCaracCel.fabricante)

print('\n4.A-Renomeie as colunas sistema operacional(SO) e tamanho tela (tela). Exiba')
print(dfCaracCel.rename(columns = {"sistema operacional" : "SO" , "tamanho tela" : "tela"}, inplace = True))
print(dfCaracCel)

print('\n4.B-Renomeie as colunas bateria ligado (bateria) e bateria repouso (autonomia). Exiba')
print(dfCaracCel.rename(columns = {"bateria ligado" : "bateria", "bateria repouso" : "autonomia"}, inplace = True))
print(dfCaracCel)

print('\n5-Crie e exiba um DF (dfCel1) so com as colunas tela,SO,fabricante')
dfCel1 = dfCaracCel[["tela", "SO", "fabricante"]]
print(dfCel1)

print('\n6-Alterar ordem das colunas: SO,fabricante,tela,camera,bateria,autonomia, peso')
dfCaracCel = dfCaracCel[["SO", "fabricante", "tela", "camera", "bateria", "autonomia", "peso"]]
print(dfCaracCel)

print('\n7-Exibir ordenado descrescentemente por tela, fabricante')
print(dfCaracCel.sort_values(["tela", "fabricante"], ascending = False))

print('\n8-Tratando NaN nas  colunas bateria e autonomia')
print('\nNas colunas bateria e autonomia NaN deve ser substituido pelo valor minimo na coluna')
dfCaracCel.fillna({"bateria" : dfCaracCel.bateria.min(), "autonomia" : dfCaracCel.autonomia.min()}, inplace = True)
print(dfCaracCel)

'''
9- Crie o dataframe dfPrecosCel a partir da planilha precos do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas.
Exiba
'''
dfPrecosCel=pd.read_excel(path, sheet_name='precos', header=0, index_col=0)
print('\n9-O dfPrecosCel')
print(dfPrecosCel)

print('\n10-Exiba as informacoes do dfPrecosCel')
dfPrecosCel.info()

print('\n11-Tratando NaN: horizaontais com preco NaN devem ser descartadas. Exiba')
print(dfPrecosCel.dropna()) #didn't do inplace because we wanted to remove the colunas in the next question


print('\n11-Tratando NaN: colunas com preco NaN devem ser descartadas. Exiba')
dfPrecosCel.dropna(axis = 1, inplace = True)
print(dfPrecosCel)


'''
12- Crie o dataframe dfNotasCel a partir da planilha avaliacao do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas.Exiba.
'''
dfNotasCel=pd.read_excel(path,sheet_name='avaliacao',header=0,index_col=0)
print('\n12-O dfNotasCel')


print('\n13-Exiba as informacoes do dfNotasCel')
dfNotasCel.info()

print('\n14-Renomeie Nota Tela (NTT), Nota Camera(NCC), Nota Desempenho (NTD)')
dfNotasCel.rename(columns = {"Nota Tela" : "NTT", "Nota Camera" : "NCC", "Nota Desempenho" : "NTD"}, inplace = True)
print(dfNotasCel)

print('\n15- Concatene os 3 dataframes, criando o dfCelular. Exiba')
dfCelular = pd.concat([dfCaracCel, dfPrecosCel, dfNotasCel], axis = 1)
print(dfCelular)

print('\n16- Incluindo Preco Medio (PrecoMed). Exiba')
dfCelular["PrecosMed"] = dfPrecosCel.mean(axis = 1)
#print(dfCelular["PrecosMed"])
print(dfCelular)

print('\n17- Incluindo Nota Global(NTG) =( 1XTela+1XCamera+2XDesempenho)/4. Exiba' )
#PESOS: 1, 1 e 2
dfCelular["NTG"] = (dfNotasCel["NTT"] + dfNotasCel["NCC"] + 2*dfNotasCel["NTD"])
#print(dfCelular["NTG"])
print(dfCelular)

print('\n----------------------------------------------------------------')
print('\n18-Graficamente (barras juntas) precos no CasaTecno e no TemTudo' )
dfCelular[["SuperCel", "TemTudo"]].plot.bar(title = "Precos em 2 sites", figsize = (8,6))
plt.show()

print('\n----------------------------------------------------------------')
'''
USE dataframe.plot.scatter(x='NomeDaColuna1', y='NomeDaColuna2') 
'''
print('\n19- Graficamente: PrecoMedio X Nota Global')
dfCelular.plot.scatter(x = "PrecosMed", y = "NTG")
plt.show()

print('\n20- Exibir os celulares com tela >= 5.7 e com preco na CasaTecno menor que 3000')
#dfResposta= dfCelular.query('tela >= 5.7 and CasaTecno <3000') #This is another form to do what is in the given line below
dfResposta = dfCelular.loc[ (dfCelular.tela>=5.7 ) & (dfCelular.CasaTecno <3000) ]
print(dfResposta)
print('APENAS OS NOMES dos Modelos que atendem o criterio')
print(dfResposta.index.values)

print('APENAS OS NOMES dos Modelos que atendem o criterio')



print('\n21-Categorias (faixas) de nota global: de 0 a 6, de 6(exc) a 7,de 7 a 8, de 8 a 9, acima de 9')
print('\n- Rotular com "RUIM", "REGULAR","BOM","MUITO BOM","EXCELENTE"')
print('\n Exibir TabFreq das categorias de nota')



#ATENCAO:
print('\nTabela de Frequencia Percentual (RELATIVA) das categorias graficamente')


#ATENCAO 2:
print('\nTabela de Frequencia Percentual (RELATIVA) das categorias NUMERICAMENTE')



print("\n22- Qual(is) o(s) celular(es) de pior desempenho?")
ntMinDesemp = dfCelular["NTD"].min()
dfCelPiorDesemp = dfCelular.loc[dfCelular["NTD"] == ntMinDesemp]
#print(dfCelPiorDesemp)
print(dfCelPiorDesemp.index.values)

print("\n23- Qual(is) o(s) celular(es) de melhor desempenho e seus precos medios?")
ntMaxDesemp = dfCelular["NTD"].max()
dfCelMelhorDesemp = dfCelular.loc[dfCelular["NTD"] == ntMaxDesemp]
#print(dfCelMelhorDesemp)
print(dfCelMelhorDesemp.index.values)


print("\n24-Qual(is) o(s) celular(es) de maior nota global , seu menor preco e onde ocorre seu menor preco")
dfCelMaiorNotaG= dfCelular.loc[dfCelular['NTG']==dfCelular['NTG'].max()]
print(dfCelMaiorNotaG)
print('\n')
dfResposta = dfPrecosCel.loc[dfCelMaiorNotaG.index]
print(dfResposta.agg(['min','idxmin'], axis=1))