from classehorario import Tempo



class Corredor:

    def __init__(self, num, name, h = 0, m = 0, s = 0):
        self.name = name
        self.num = num
        self.tempo = Tempo(h, m, s)

    def __str__(self):
        s = f"Nome: {self.name}, Numero: {self.num}, Tempo: {self.tempo}"
        return s
    
    def __repr__(self):
        r = "{} - {} - {}".format(self.name, self.num, self.tempo)
        return r

    def maisRapido(self, outro):
        return self.tempo < outro.tempo
            

def vencedorDaCorrida(l):
    fastest = l[0]
    for person in l[1:]:
        if fastest.maisRapido(person):
            fastest = person
    print("\n---Winner---")
    print(fastest)



c1 = Corredor(222,'Buba',2,30,15)
c2 = Corredor(999,'Nana',1,35,20)
c3 = Corredor(666,'Lulu',1,20,40)
c4 = Corredor(777,'Vivi',2,10,12)
lcorredores = [c1,c2,c3,c4]

print(lcorredores)

print(c1)

print("\nList of runners", lcorredores)

print("\nFastest between the two runners:")
if c1.maisRapido(c2):
    print(c1, "mais rapido que", c2)
else:
    print(c2, "mais rapido que", c1)

vencedorDaCorrida(lcorredores)