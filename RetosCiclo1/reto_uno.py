
peso_chavo = float(input("ingrese el peso de chavo:"))
peso_chavo_entero = int(peso_chavo)

peso_quico = (peso_chavo_entero * 2) + 4
peso_ñoño = (peso_quico + peso_chavo_entero) // 5
etapa = ""
if(peso_chavo_entero > 0):
  if(peso_ñoño > 0 and peso_ñoño <= 20):
    etapa = "uno"
  elif(peso_ñoño >= 21 and peso_ñoño <= 40):
    etapa = "dos"
  elif(peso_ñoño >= 41 and peso_ñoño < 80):
    etapa = "tres"
  else:
    etapa = "cuatro"
  print(peso_chavo_entero, " ", peso_quico, " ", peso_ñoño)
  print(etapa)
else:
  print("usted ingreso un valor negativo por favor intente de nuevo")
