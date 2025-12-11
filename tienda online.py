















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



class Cliente:

    def __init__(self, nome_cliente, email, direccion,codpostal):
        self.__nome = self.setNome(nome_cliente)
        self.__email = self.setEmail(email)
        self.__direccion = self.setDireccion(direccion)
        self.__codpostal = self.setCodPostal(codpostal)

    def setNome(self, nome_cliente):
        if isinstance(nome_cliente, str):
            return nome_cliente
        else:
            nome_cliente = None
            return nome_cliente

    def setEmail(self, email):
        if isinstance(email, str):
            for n in email:
                if n == "@":
                    return email
        else:
            email = None
            return email

    def setDireccion(self, direccion):
        if isinstance(direccion, str):
            return direccion
        else:
            direccion = None
            return direccion

    def setCodPostal(self, codpostal):
        if isinstance(codpostal, int):
            return codpostal
        else:
            codpostal = None
            return codpostal


    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getDireccion(self ):
        return self.__direccion

    def getCodPostal(self):
        return self.__codpostal

    def aCadea(self):
        cadea = "\n\t nome : " + str(self.__nome) + "\n\t email: " + str(self.__email) + "\n\t direccion: " + str(
            self.__direccion + "\n\t codpostal: " + str(self.__codpostal))
        return cadea


horario = Cliente("Juan", "hola@", "que tal", 45)
print( horario.aCadea())