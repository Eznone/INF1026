# Autor: Claudia Ferlin
# A classe Horario a seguir representa um horario (ou um periodo de tempo).
# Um horario tem hora, minuto e segundo.
# Um horario eh criado sendo fornecidos hora, minuto e segundo.
# Nao sendo fornecido valor para hora ou minuto ou segundo, considera-se 0.
# Um horario deve ser exibido no formato hh:mm:ss
# Deseja-se consultar  hora ou  minuto ou segundo de um horario.
# Deseja-se poder alterar hora ou minuto ou segundo de um horario.
# Eh possivel comparar dois horarios (> , < , ==, !=).
# Eh possivel calcular a soma de dois horarios.
# Eh possivel calcular a diferenca entre dois horarios.

# OBS: Para as operacoes de comparacao eh conveniente termos o tempo total 
# em segundos que corresponde a esse horario. Podemos disponibilizar uma
# funcao para calcular e retornar o tempo em segundos ou, deixar como um
# atributo dentro do objeto.


class Horario:
    def __init__(self, h=0,m=0,s=0):
        self.hora = int(h)
        self.min = int(m)
        self.seg = int(s)
        self.tempo = self.hora*3600+self.min*60 + self.seg
        return
    def __str__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    
    def __repr__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    
    # para comparar
    def __eq__(self,outro):
        return(self.tempo==outro.tempo)
    def __ne__(self,outro):
        return(self.tempo != outro.tempo)
    def __lt__(self,outro):
        return(self.tempo<outro.tempo)
    def __gt__(self,outro):
        return(self.tempo>outro.tempo)

    # para somar/calcular diferenca de dois horarios
    def __add__(self,outro):
        tot=abs(self.tempo+outro.tempo)
        return self.geraHorario(tot)
    
    def __sub__(self,outro):
        dif=abs(self.tempo-outro.tempo)
        return self.geraHorario(dif)

    #para alterar h ou m ou s
    def setSeg(self,s):
        self.seg=s
        self.tempo = self.hora*3600+self.min*60 + self.seg
    def setMin(self,m):
        self.min=m
        self.tempo = self.hora*3600+self.min*60 + self.seg
    def setHora(self,h):
        self.hora=h
        self.tempo = self.hora*3600+self.min*60 + self.seg

    #para consultar h ou m ou s
    def getSeg(self):
        return self.seg
    def getMin(self):
        return self.min
    def getHora(self):
        return self.hora
    
    # funções auxiliares

    # funcao auxiliar geraHorario a ser utilizada em __add__ e __sub__,
    # cria um novo objeto da classe Horario a partir de um tempo total
    # em segundos recebido
    def geraHorario(self,tempo):
        h=tempo//3600
        m=tempo%3600//60
        s=tempo%3600%60
        return Horario(h,m,s)
'''
h1=Horario(2,13)
print(h1)
h2= Horario(1,2,3)
print(h2)
lh=[h1,h2]
print(lh)
'''