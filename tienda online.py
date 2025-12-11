from cliente import Cliente
from producto import Producto

class Pedido:
    def __init__(self,data):
        self.cestaProducto = list()
        self.cliente = str()
        self.data = data


    def getCestaPedido(self):
        return self.cestaProducto

    def getCliente(self):
        return self.cliente

    def getData(self):
        return self.data
    def setCantidade(self, cantidade):
        if isinstance(cantidade,int):
            if cantidade >= 0:
                return cantidade
            else:
                cantidade = 0
                return cantidade
        else:
            cantidade=0
            return cantidade

    def engadirProducto(self,cantidade,producto):
        if producto.getCantStock >= cantidade:
            self.cestaProducto.append ((producto, cantidade))
            producto.decrementarStock(cantidade)

    def calculoPrezoTotal(self):
        total = 0
        for entrada in self.cestaProducto:
            total = total + entrada[1] * entrada[0].getPrezo()
        return

p = Pedido(Cliente("h","@","d",34),Producto("h",34, 35),"22")

print(p)





