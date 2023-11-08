



class Tempo:

    def __init__(self, hour, min, sec):

        self.hour = int(hour)
        self.min = int(min)
        self.sec = int(sec)
        self.totTime = self.hour * 3600 + self.min * 60 + self.sec 


    def __str__(self):
        s = "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hour, self.min, self.sec)
        return s
    
    #Dont actually need this repr as the the repr in the meucorredor already takes care of it being a list
    def __repr__(self):
        r = "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hour, self.min, self.sec)
        return r

    def __lt__(self, outro):
        return self.totTime < outro.totTime