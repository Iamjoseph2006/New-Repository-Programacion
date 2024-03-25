# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt en modo escritura ('w')
file = open('my_notes.txt', 'w')
file.write("Primera línea de notas\n")
file.write("Segunda línea de notas\n")
file.write("Tercera línea de notas\n")
file.close()  # Cerrar el archivo después de escribir en él

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt en modo lectura ('r')
file = open('my_notes.txt', 'r')
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()  # Cerrar el archivo después de leerlo