# numero_uno = 20
# numero_dos = 2
# numero_tres = 15
# numero_cuatro = None
# resultado = ""
#
# if numero_uno > numero_dos:
#     resultado = f"el numero {numero_uno} es mayor a numero {numero_dos}"
#     if numero_uno > numero_tres:
#         resultado = resultado+ f" y mayor que numero {numero_tres}"
#     else:
#         resultado = resultado + f" y {numero_uno} es menor que numero {numero_tres}"
# else:
#     resultado = "El numero dos es mayor"
#     numero_uno = 5
#     numero_dos = 4
#     numero_tres = 12
#     numero_cuatro = 6
#
#
# print(f"El resultado es: {resultado}")

# Matrices
# matriz_numeros = [[1, -3, 2], [4, 11, -1]]
# def cuadrados_matriz ():
#     X = [[1, -3, 2], [4, 11, -1]]
#     Y = [ ]
#     for i in range(len(X)):
#         fila = []
#         for j in range(len(X[i])):
#             fila.append(X[i][j]*X[i][j])
#         Y.append(fila)
#     return Y
# print(cuadrados_matriz())

# s1 = "Falta mucho? \n" * 5
# print(s1)
#
# s2 = "¿hemos llegado ya?\n" * 5
# print(s2)

# print("ingrese el nombre del destinatario")
# name =input()
#
# s1 = "¡cumpleaños feliz!"
# s2 = "Te deseamos "
#
# song = (s1 + "\n") * 2 + s2 + name + ",\n" + s1
# print(song)

# nombre = "javier"
# edad = 21
# print("mi hernao se llamada", nombre, "y su edad es " + str(edad))

# nombre = "ricardo"
# numero_gatos = 2
# print("Mi abuelo se llama {} y tiene {} gatos".format(nombre, numero_gatos ))

# #
# s = "SOY FAN DE LOS VIDEOJUEGOS"
# print(s[-2])
# print(s[5])
# print(s[4:7])
# print(s[:7])
# print(s[8:])
# print(s[-10:])
# print(s[:-10])

# #  RETO 4
# import json
# entrada = input("Ingrese el diccionario de criptos : ")
# entrada = json.loads(entrada)
# print(entrada)
# print(type(entrada))
# entradas = str({"SOL": 50, "BTC": 29000, "DOT": 0.2, "SHIBA": 0.0354, "LUNA": 2, "APE": 35})
#
#
# # entrada=entrada.replace('"','')
# # entrada=entrada.replace(':',' ')
# # entrada=entrada.replace(',',' ')
# # print(entrada)

# nombre = "Diana"
# Apellidos = "Zipa"
# Edad = 29
# print(nombre, Apellidos,Edad)


#
# resultantList = []
#
# for element in myList:
#     if element not in resultantList:
#         resultantList.append(element)
#
# print(resultantList)
#
#
#
# tipodefigurita(['mamiferos','plantas','peces','mamiferos','paisajes','plantas','microbios','peces','microbios', 'plantas'])
# mefaltatipodefigura([3,6,8], [ 'plantas', 'mamiferos', 'paisajes', 'mamiferos', 'paisajes','mamiferos','microbios','peces','mamiferos'], "mamiferos" )
# puedocambiar([3,5,7,10,15,16],[4,10,5,8])
# notengo([2,4,5,7,11,14], [11,4,7])


# Ejercicio String: Dado un Stirng vamoa a pedir al usuario que introduzca la palabra perteneciente
# a dicho string y vamos a obtener el substring sin la palabra indicada por el usuario utilizando el metodo
# .fin y la funcion .len

# sentence = "El camino esta cerrado pero seguro podremos encontrar una alternativva"
# print("esta es la frase original: ", end =  " " )
# print(sentence)
# 
# print("introduce la palabra original que queiras eliminar: ")
# word = input("palabra: ")
#
# idx = sentence.find(word) #con .find se puede tomar el indice de la palabra word osea tomamos la W
# sentence2 = sentence[:idx] + sentence[idx + len(word) + 1 :]
# print(sentence2)

# devolver la palabra en mayuscula
# print("introduce una palabra y yo te la devuelvo en mayuscula")
# word = input()
# print(word.upper())

# devolver la frase con todas las palabras empezando en mayuscula
# print("introduce una frase y yo te devuelvo todas las palabras empezando mayuscula")
# s = input()
# print(s.title())

# # Devolver la palabra (con 3 o mas letras) con todas las letras en miniscula salvo la tercera letra
# print("introduce una palabra con tres letras o mas y yo te devuelvo todas sus letras en minuscula salvo la tercera")
# word = input()
# print(word[:2].lower() + word[2].upper() + word[3:].lower())

# Devolver la palabra con todas las letras en mayúsculas salvo la primera y la última
# print("introduce una palabra y yo te devolvere toda en mayuscula salvo la primera y la ultima")
# word = input()
# print(word[0].lower() + word[1:(len(word) - 1)].upper() + word[-1].lower())

# # Devolver la frase donde cada vez que aparezcan las dos primeras letras de la primera palabra, sean substituidas por cualesquiera otras dos letras.
# subs = "PI"
# print("Introduce una frase y yo te la devuelvo sustituyendo las dos primeras letras de la primera palabra por las letras {}".format(subs))
# s = input()
# print(s.replace(s[:2], subs))

# # Vamos a pedirle al usuario su año de nacimiento y el año actual y le vamos a imprimir por pantalla su edad
# year = int(input("Introduce tu año de nacimiento"))
# this_year = int(input("Introduce el año actual"))
# age = this_year - year
# print("en el año {} tienes {} años".format(this_year,age))


# Dado un string, vamos a comprobar si contiene espacios en blanco y en caso de ser cierto contaremos cuantos tiene

# s = "mi gato mola mucho"
# c = " "
# if c in s:
#     print("el string tiene {} espacios en blanco". format(s.count(c)))

# Vamos a hacer un programa que resuelva ecuaciones de primer grado de la forma Ax + B = 0 proporcioandas por el susuario donde A sea diferente que 0

# a = float(input("coeficiente A = "))
# b = float(input("coeficiente B = "))
# if a != 0:
#     sol = -b / a
#     print("la solución es X =", sol)
#     print("la solución es X =", sol)
# else:
#     print("No hay ecuacion que resolver, porque A es menor que 0")

# COMPROBAR SI UN NUMERO ES PAR O IMPAR
# n = 10
# message = "El numero es Par" if n % 2 == 0 else "el numero es impar"
# print(message)
#  Comprobando si un punto X, Y pertenecen al cuadro unidad

# x = float(input("X =  "))
# y = float(input("Y =  "))
#
# if x >= 0 and x <= 1 and y >= 0 and y <=1:
#     print("el punto ({}, {}) se encuentran en el cuadro unidad ".format(x, y))
# else:
#     print("el punto ({}, {}) no pertenece al cuadro unidad ".format(x, y))

# ("el punto ({}, {}) se encuentran en el cuadro unidad ".format(x, y))

# Vamos a comprobar si el año es bisiesto o no un año es bisiesto si es divisible entre cuatro
# pero no es multiplo de 100 a no ser que lo sea de 400

# year = int(input("Años: "))
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("el Año {} es bisiesto".format(year))
#         else: print("el año {} no es bisiesto".format(year))
#     else: print("el año {} es bisiesto".format(year))
# else: print("el año {} no es bisiesto".format(year))



a = 5
b = 2
print(float(a) % float(b))



