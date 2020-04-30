from io import open



archivo_texto = open('archivo.txt', 'w') #'w' para abrir en modo escritura
frase='- Hola Padre Karras. Excelente día para un exorcismo.'
archivo_texto.write(frase)
archivo_texto.close()

#############

archivo_texto=open('archivo.txt', 'r')
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

#############

archivo_texto=open('archivo.txt', 'r')
lineas_texto=archivo_texto.readlines() #Lee línea a línea y lo almacena en una lista.
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])

#############

archivo_texto=open('archivo.txt', 'a') #'a'-> append
archivo_texto.write('\n\n- Pero mira que eres perra')
archivo_texto.close()
print(texto)

#############

archivo_texto=open('archivo.txt', 'r')
print('\n\n\n', archivo_texto.read())

#Si se abre un archivo, el puntero está al inicio.
#Al leer el archivo, se situa al final, por lo que ya no leería nada.

print('\n\n\n', archivo_texto.read()) #No imprime nada al estar el cursor al final
print('__No aparece nada\n')
archivo_texto.seek(0)

print(archivo_texto.read())

print('\n__Cursor en medio\n')
archivo_texto.seek(23)

print(archivo_texto.read())
archivo_texto.seek(0)
#seek() posiciona el puntero. con read() podemos leeer a partir de la posición idnicada

print(archivo_texto.read(10)) #Lee hasta la posición 10 y si repetimos leería desde ahí

###############

#xej colcar cursor a mitad de texto:
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

###############
archivo_texto=open('archivo.txt', 'r+') #r+ = lectura y escritura


###############

archivo_texto.close()