def registrar_habitos():
    agregar = input("Quiere agregar? ") 
    while True:
        if agregar == "si":
            actividades = input("Ingrese actividad: ")
            lista_act = []
            lista_act.append(actividades)
            agregar = input("Quiere agregar? ")
        elif agregar == "no":
            break
        
        