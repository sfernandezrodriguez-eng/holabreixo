


class Producto:
    def __init__(self,nome,prezo,cantStock):
        self.__nome=self.setNome(nome)
        self.__prezo=self.setPrezo(prezo)
        self.__cantStock=self.setCantStock(cantStock)

    def setNome(self,nome):
        if isinstance(nome, str):
            return nome
        else:
            nome= None
            return nome

    def setPrezo(self, prezo):
        if isinstance(prezo, int) or isinstance(prezo, float) :
            if prezo >= 0:
                return prezo
            else:
                prezo = 0
                return prezo
        else:
            prezo=0
            return prezo

    def setCantStock(self, cantStock):
        if isinstance(cantStock,int):
            if cantStock >= 0:
                return cantStock
            else:
                cantStock = 0
                return cantStock
        else:
            cantStock=0
            return cantStock
    def getNome(self):
        return self.__nome
    def getPrezo(self):
        return self.__prezo
    def getCantStock(self,):
        return self.__cantStock
    def decrementarStock(self,cantStock):
         self.__cantStock = self.__cantStock - cantStock

    def incrementarStock(self,cantStock):
        self.__cantStock = self.__cantStock + cantStock
    def aCadea(self):
        cadea = "\n\t nome : " + str(self.__nome) + "\n\t prezo: " + str(self.__prezo) + "\n\t cantStock: " + str(self.__cantStock)
        return cadea

horario = Producto("Juan",44,5)
print( horario.incrementarStock(5) ,horario.aCadea())