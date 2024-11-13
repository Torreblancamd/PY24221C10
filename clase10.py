
class Perro:


    def __init__(self, nombre_perro , edad_perro , color_perro , raza_perro , duenio=None ):
        #PROPIEDAS
        self.nombre = nombre_perro
        self.edad = edad_perro
        self.color = color_perro
        self.raza = raza_perro
        self.duenio = duenio

    #METODO
    def ladrar(self):
        print(self.nombre, ": GUA GUA GUA")


    def get_datos(self):
        print("<--- PERRO: --->")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Color: {self.color}")
        print(f"Raza: {self.raza}")
        print(f"Dueño: {self.duenio}")
        print("")



    def set_duenio(self, nombre_duenio:str):#TYPE HINT
        if type(nombre_duenio) == str:
            self.duenio = nombre_duenio
        else:
            print("Tipo de dato incorrecto")


perro_uno = Perro("Fatiga",10,"Marron","Dogo","Pepe")
perro_dos = Perro("Coraje", 5 , "Violeta", "Pepe")

print( perro_uno )


#OPERADOR DOT

print(perro_uno.nombre)
print("Edad perro uno: ", perro_uno.edad)

print("Nombre del perro dos: ", perro_dos.nombre)



perro_uno.ladrar()
perro_dos.ladrar()

#TRAER DATOS DEL PERRO

perro_uno.get_datos()
perro_dos.get_datos()


#CAMBIAMOS EL NOMBRE DEL DUEÑO AL PERRO 2
perro_dos.set_duenio()


perro_dos.get_datos()