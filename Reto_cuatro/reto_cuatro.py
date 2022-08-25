import json
criptos = input()
digital_wallet = input()
digital_wallet += " "
criptos = json.loads(criptos)
cripto = ""
concidences = ""
money = 0
for wallet in digital_wallet:
    if wallet == " ":
        if cripto in criptos:
            money += criptos.get(cripto)
            concidences += cripto + " "
        cripto = ""
    else:
        cripto += wallet
if len(concidences) > 0:
    print(concidences[:-1])

print(money)














