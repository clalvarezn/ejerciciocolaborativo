# Opcion 2


if Opción == "2":
    busqueda_rut = input("Ingrese el rut a buscar: ")
    encontrado = False
    for af in datosclientes:
        if af["rut"] == busqueda_rut:
            print("Afiliado encontrado")
            print("Nombre",af["nombre"])
            print("Apellido", af["apellido_paterno"])
            print("Edad", af["edad"])
            print("Estado Civil", af["estado_civil"])
            print("Genero", af["genero"])
            print("Fecha de afiliación", af["fecha_afiliacion"])
            encontrado = True
            break
        if not encontrado:
            print("Afiliado no encontrado")



    



