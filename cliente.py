


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


horario = Cliente("Juan", "hola", "que tal", 45)
print( horario.aCadea())