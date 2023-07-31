ARCHIVO_RECUERDOS_PERSONA = "recuerdos_persona.txt"

#Pre: que alla un nombre para buscar, sino no se encontrara nada
#Pos: devuelve los recuerdos de la persona elegida.

def separar_recuerdos(personas, recuerdos_de_personas, nombre_buscado):
    try:
        archivo = open(personas, "r")
    except:
        print(f"No se pudo habrir {personas}")
        return
    try:
        recuerdos = open(recuerdos_de_personas, "r")
    except:
        print(f"No se pudo habrir {recuerdos_de_personas}")
        return
    try:
        recuerdos_elegidos = open(ARCHIVO_RECUERDOS_PERSONA, "w")
        vector = []
        for linea in archivo:
            persona = linea.strip().split(";")
            id_persona = persona[0]
            nombre_persona = persona[1]
            if(nombre_persona == nombre_buscado):
                id_indicado = id_persona
        for recuerdo in recuerdos:
                    momento = recuerdo.strip().split(";")
                    id_momento = momento[0]
                    nombre_momento = momento[1]
                    if(id_momento == id_indicado):
                        vector.append(nombre_momento)
        for linea in vector:
            recuerdos_elegidos.write(linea.strip())


        recuerdos_elegidos.close()
        archivo.close()
        recuerdos.close()
    except:
        archivo.close()
        recuerdos.close()
        recuerdos_elegidos.close()
    

