# Creamos un objeto de tipo biblioteca
from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libro import Libro

bibliotecaMexico = Biblioteca('Biblioteca México')

# Agregar algunos libros
libro1 = Libro('El Alquimista', 'Paulo Cohelo', 'Ficción')
libro2 = Libro('1984', 'George Orwell', 'Ficción')
libro3 = Libro('El código Da Vinci', 'Dan Brown', 'Misterio')
libro4 = Libro('Rayuela', 'Julio Cortázar', 'Novela')
libro5 = Libro('Verónica decide morir', 'Paulo Cohelo', 'Ficción')
# Agregar los libros a la biblioteca
bibliotecaMexico.agregar_libro(libro1)
bibliotecaMexico.agregar_libro(libro2)
bibliotecaMexico.agregar_libro(libro3)
bibliotecaMexico.agregar_libro(libro4)
bibliotecaMexico.agregar_libro(libro5)

# Nombre de la biblioteca
print(f'*** Bienvenidos a la {bibliotecaMexico.nombre} ***')

# Buscar libros por autor
print(f'\nLibros de Paulo Cohelo: ')
bibliotecaMexico.buscar_libros_por_autor('Paulo Cohelo')

# Buscar libros por género
print(f'\nLibros de Ficción: ')
bibliotecaMexico.buscar_libros_por_genero('Ficción')

# Mostrar todos los libros de la biblioteca
bibliotecaMexico.mostrar_todos_los_libros()

