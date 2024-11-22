#Crear una clase llamada Alumno
#Propiedades: nombre , dni , nota_uno , nota_dos
#Los datos de nota_uno y nota_dos no se tienen cuando se crea el alumno
#Crear un metodo que imprima todos los datos de los alumnos: get_datos
#Crear un metodo que setea la nota_uno: set_nota_uno
#Crear un metodo que setea la nota_dos: set_nota_dos
#Crear un metodo que muestre el estado del alumno/a: get_estado-->RECURSA(1,2,3),RECUPERA(4,5,6),APROBADO(7,8,9,10)


#EXTRA POINT
#MODIFICAR sacar las propiedades nota_uno y nota_dos
# Ahora la propiedad es materias y cada materia tiene sus 2 notas + promedio final



class Alumno:

    def __init__(self, nombre:str , dni:int):
        self.nombre = nombre
        self.dni = dni
        self.nota_uno = 0
        self.nota_dos = 0

    
    def __str__(self):
        return f"Nombre: {self.nombre} DNI: {self.dni}"


    def get_datos(self):
        print("<--- Alumno: --->")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Nota uno: {self.nota_uno}")
        print(f"Nota dos: {self.nota_dos}")       
        print("")


    def set_nota_uno(self, nota:float):
        if nota >= 1 and nota <= 10 and type(nota) == float:
            self.nota_uno = nota
        else:
            print(f"Error cargando la nota: {nota}")


    def set_nota_dos(self, nota:float):
        if nota >= 1 and nota <= 10 and type(nota) == float:
            self.nota_dos = nota
        else:
            print(f"Error cargando la nota: {nota}")



    def get_estado(self):
        if self.nota_uno != 0 and self.nota_dos != 0:
            print(f"Alumno:{self.dni} ")
            promedio = (self.nota_uno + self.nota_dos)/2
            print(f"PROMEDIO: {promedio}")
            if promedio >= 7 and promedio <= 10:
                print("Estado: APROBADO")
            elif promedio >= 4:
                print("Estado: RECUPERA")
            else:
                print("Estado: RECURSA")
        else: 
            print("Falta cargar las notas")


alumno_uno = Alumno("Pepe", 321312323)
print(alumno_uno)

alumno_uno.get_datos()


#SETEAR PROPIEDAS
#alumno_uno.nota_uno = 10
#alumno_uno.nota_dos = 27

alumno_uno.set_nota_uno(3.0)
alumno_uno.set_nota_dos(1.5)

alumno_uno.get_datos()


alumno_uno.get_estado()