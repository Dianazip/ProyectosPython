def tipodefigura(temas):
    result = []
    for tema in temas:
        if tema not in result:
            result.append(tema)
    return result

def mefaltatipodefigura(meFalta,temas2, no_tengo):
    resultado = []
    for falta in meFalta:
        if no_tengo == temas2[falta]:
            resultado.append(falta)
    return resultado

def notengo(persona1, fan):
    interesado = []
    for persona in persona1:
        if persona not in fan:
            interesado.append(persona)
    return interesado

def puedoCambiar(interesado1, interesado2):
    interesados = []
    for interesado in interesado2:
        if interesado not in interesado1:
            interesados.append(interesado)
    return (len (interesados))