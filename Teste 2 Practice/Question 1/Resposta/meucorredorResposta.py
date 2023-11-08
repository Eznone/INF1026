# -*- coding: utf-8 -*-

"""
Created on Sun Oct  4 20:17:39 2020

@author: Joisa
"""
from classehorarioResposta import Horario 

#  SOLUCAO Q1: classe Corredor
class Corredor:
                                
    def __init__ (self,num, nome,h=0,m=0,s=0):
        self.numero = num
        self.nome = nome
        self.tempo = Horario(h,m,s)
        
    def __str__ (self):
        s = 'Numero:{} - Nome:{} - Tempo:{}'.format(self.numero,self.nome,self.tempo)
        return s
    
    # EXTRA
    def __repr__(self):  # nao pedido
        s = '{} - {} - {}'.format(self.numero,self.nome,self.tempo)
        return s
    
    def maisRapido(self,outro):
        return self.tempo<outro.tempo
    
    # EXTRA EXTRA:
    # se quisermos comparar diretamente dois corredores 
    # qual o criterio?? poderia ser nome, poderia ser tempo...
    def __lt__(self, outroCorredor):
        return self.tempo<outroCorredor.tempo
    
#---------------------  fim da classe Corredor -----------------
  
#  SOLUCAO Q2: função vencedorDaCorrida
def vencedorDaCorrida(lcorred):
    if (len(lcorred))==0:
        return None
    venc=lcorred[0]
    for corredor in lcorred[1:] :
        if corredor.maisRapido(venc):
            venc = corredor
    print(venc)

 
# PRINCIPAL: retire os comentários para testar suas respostas

c1 = Corredor(222,'Buba',2,30,15)
print(c1)
c2 = Corredor(999,'Nana',1,35,20) 
print(c2)

if c1.maisRapido(c2):
    print(c1, ' mais rapido do que ', c2)
else:
    print(c2, ' mais rapido do que ', c1)
    
print(c1<c2)

c3 = Corredor(666,'Lulu',1,20,40) 
c4 = Corredor(777,'Vivi',2,10,12) 
# # print(c1)
 
lcorredores = [c1,c2,c3,c4] 
print('---- Lista ----')
print(lcorredores)

print('\nVencedor:')
vencedorDaCorrida(lcorredores)

# print('---- Lista Ordenada Crescentemente ----')
# #lcorredores.sort( ) #vai alterar a lista, deixando-a ordenada
# print(sorted(lcorredores)) # exibe ordenada

# print('---- Lista Ordenada Decrescentemente ----')
# #lcorredores.sort(reverse=True)  #altera a lista
# print(sorted(lcorredores, reverse=True))

# print('---- Lista ----')
# print(lcorredores)
