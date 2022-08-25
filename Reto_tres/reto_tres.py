botones_permitidos = ["L", "R", "X", "A", "B", "Y"]
botones_ingresados = input()
botones_ingresados = botones_ingresados.upper()
botones_ingresados = botones_ingresados.replace(",", "")
botones_ingresados = botones_ingresados.replace(" ", "")
contador = 0
botones_contados = ""
orden_botones = ""
validar_proceso = True

for boton in botones_ingresados:
    if boton in botones_permitidos:
        if orden_botones == "":
            orden_botones += boton + " "
            contador += 1
        elif orden_botones[-2] != boton:
            orden_botones += boton + " "
            botones_contados += str(contador) + " "
            contador = 0
            contador += 1
        else:
            contador += 1
            pass
    else:
        validar_proceso = False
        break
if validar_proceso:
    botones_contados += str(contador)
    print(orden_botones)
    print(botones_contados)




















