

class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def setAno(self,ano):
        if type(ano) == int:
            if ano > 0:
                self.ano = ano
                return self.ano
            else:
                self.ano = 0
                return self.ano

    def setMes(self,mes):
        if type(mes) == int:
            if mes > 0 and mes< 13:
                self.mes = mes
                return self.mes
            else:

                self.mes = 0
                return self.mes


    def setDia(self, dia):
        if type(dia) == int:
            if dia > 0 and dia < 32:
                self.dia = dia
                return self.dia
            else:
                self.dia = 0
                return self.dia

    def setComprobar(self,dia,mes,ano):
        if type(dia) == 0 or type(mes) == 0 or type(ano) == 0:
            dia = 0
            mes = 0
            ano = 0
        if mes == 2:
            if dia< 28 or dia>0:
                self.__dia = 0
                self.__mes = 0
                self.__ano = 0
        return self.dia, self.mes, self.ano
    def getAno(self):
        return self.__ano

    def getMes(self):
        return self.__mes

    def getDia(self):
        return self.__dia
    def getComprobar(self):
        return self.dia, self.mes, self.ano

    def aCadea(self):
        cadeaData= "Horario: \n\t dia= "+ str(self.dia) + "\n\t mes = "+ str(self.mes) + "\n\t ano = "+ str(self.ano)
        return cadeaData


data = Data(30,2,2001)
print(data.aCadea())
data.dia = 42
print (data.dia)

