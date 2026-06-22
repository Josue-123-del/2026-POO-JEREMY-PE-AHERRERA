from modelos.productos import Producto
from modelos.clientes import Cliente
from servicios.restaurante import Restaurante

producto1 = Producto("HOT DOG", 3.50, "Comida")
producto2 = Producto("Chuzo", 2.00, "Comida")
producto3 = Producto("Inca cola", 1.50, "Bebida")

cliente1 = Cliente("Pedro Nieto", "1234567890", "0999999999")
cliente2 = Cliente("Geidy Freire", "0987654321", "0888888888")

mi_restaurante = Restaurante()

mi_restaurante.agregar_producto(producto1)
mi_restaurante.agregar_producto(producto2)
mi_restaurante.agregar_producto(producto3)

mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)

mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()   
