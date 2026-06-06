class Estudiante:
    def _init_(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")  

estudiante1 = Estudiante("Jeremy Peñaherrera", 24, "Ingeniería en tic")                    
estudiante1.mostrar_informacion()
print("\n")
estudiante2 = Estudiante("Geidy Freire ", 25, "turismo")
estudiante2.mostrar_informacion()
