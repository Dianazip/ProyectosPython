jugadores_disponibles = [".", "+", "T", "|", "X", "-", "*", "Y", "W", "!", "@", "#", "$"]
cobradores_validos=True
cobradores_ingresados = []
porteros_validos = True
porteros = ""
resultados = ""
print(f"los jugadores disponibles son: {jugadores_disponibles}")
cobradores_penal = input()
if (len(cobradores_penal) >=1 and len(cobradores_penal) <=6):
    for cobrador in cobradores_penal:
        if cobrador not in jugadores_disponibles:
            # validamos que lo ingresado no esta en la lista de jugadores disponibles
            print(f"jugador '{cobrador}' no es jugador disponible")
            cobradores_validos = False
            break
        elif cobrador in cobradores_ingresados:
            cobradores_validos = False
            print(f"el cobrador {cobrador} esta repetido ")
            break
        else:
            cobradores_ingresados.append(cobrador)

    if cobradores_validos:
        porteros = input()
        porteros_ingresados = []
        for portero in porteros:
            if portero not in jugadores_disponibles:
                print(f"portero '{portero}' no es jugador disponible")
                porteros_validos = False
                break
            elif portero in porteros_ingresados:
                porteros_validos = False
                print(f"el portero {portero} esta repetido")
                break
            else:
                porteros_ingresados.append(portero)
        # else:
        #     porteros_validos = False
        #     print("la cantidad de porteros debe ser igual a la cantidad de cobradores de penales")

    if cobradores_validos and porteros_validos:
        nombre_equipo = input("Ingrese el nombre del equipo:")
        nombre_equipo = nombre_equipo.lower() # cambia a minusculas el valor de la variable
        nombre_equipo = nombre_equipo.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        print(nombre_equipo)
        mayor_cantidad_goles = 0
        for cobrador in cobradores_penal:
            cantidad_goles = 0
            for portero in porteros:
                if cobrador > portero:
                    resultados = resultados + "\u00D8"
                    cantidad_goles = cantidad_goles + 1
                elif cobrador < portero:
                    resultados = resultados + "\u00A5"
                else:
                    resultados = resultados + "\u265E"
            if cantidad_goles > mayor_cantidad_goles:
                mayor_cantidad_goles = cantidad_goles
        print(resultados)

        validacion_nombre = nombre_equipo.replace(" ", "")
        if str(validacion_nombre) == str(validacion_nombre[::-1]):
            print("ES PALINDROMO")
        else:
            print("NO ES PALINDROMO")
        print(mayor_cantidad_goles)
else:
    print("numero de jugadores inavlido.")
