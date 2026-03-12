def registrar_habitos():
    '''
    Función que le pregunta al usuario actividades y las guarda en una lista.

    Returns
    -------
    lista_act : lista
        Lista de actividades.

    '''
    agregar = input("Quiere agregar? ") 
    lista_act = []
    while True:
        if agregar == "si":
            actividades = input("Ingrese actividad: ")
            lista_act.append(actividades)
            agregar = input("Quiere agregar? ")
        elif agregar == "no":
            break  
    return lista_act
        



def analizar_habitos(lista):
    '''
    Función que cuenta la cantidad de veces que aparece un elemento en una lista y los guarda en un diccionario.

    Parameters
    ----------
    lista : lista
        Lista de actividades.

    Returns
    -------
    dicc_act : diccionario
        Diccionario cuyas claves son las actividades y valores son la cantidad de veces que aparecían en la lista.

    '''
    dicc_act = {}
    for actividad in lista:
        if actividad not in dicc_act:
            dicc_act[actividad]=1
        else:
            dicc_act[actividad]+=1
    return dicc_act

            