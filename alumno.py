
from metodo_persoa import Persoa


class Alumno (Persoa):
    contar = 0
    def __init__(self,nome,edade,dni,direccion,nacionalidade,ciclo):
        super().__init__ (nome,edade,dni,direccion,nacionalidade)
        self.ciclo = ciclo
        self.sumar()
    def sumar(self):
        Alumno.contar += 1
    def  __del__(self):
        Alumno.contar -= 1




manuel= Alumno("manuel",19, "00000000X","Garcia Barbon","española", "DAM" )

paca= Alumno("manuel",19, "00000000X","Garcia Barbon","española", "DAM" )


pedro= Alumno("manuel",19, "00000000X","Garcia Barbon","española", "DAM" )

del (pedro)
print(manuel.contar)