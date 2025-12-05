
from circulo import Circulo
from Punto2 import Punto2
from metodo_persoa import Persoa
from cilindro import Cilindro
from cono import Cono
from esfera import Esfera
p1 = Punto2(2,3)
p2 = Punto2(9,1)
p3 = Punto2(5,10)
p4 = Punto2(7,6)

print(p1.aCadea(),p2.aCadea(),p3.aCadea())

manuel= Persoa("manuel",dni="00000000X", edade=19,direccion="Garcia Barbon",nacionalidade="española" )
Pablo= Persoa("Pablo",  dni="00000000X", edade=19,direccion="hi",nacionalidade="española" )
print(manuel == Pablo)


circulo= Circulo( 3,4,5)
print(circulo.aCadea())

cilindro = Cilindro(3,2,3,5)
print(cilindro.aCadea(),"area : ",cilindro.obtenerArea(5),"volumen : ",cilindro.obtenerVolumen(9))
cono = Cono(2,3,4,6)
print("cono",cono.aCadea(),"superficie : ",cono.obtenerSupercifie(5),"volumen : ",cono.obtenerVolumen(9),"generatriz : ",cono.obtenerGeneratriz(6))
esfera = Esfera(2,3,4)
print("esfera",esfera.aCadea(),"superficie : ",esfera.obtenerSupercifie(),"volumen : ",esfera.obtenerVolumen())