# Opcion 2


elif opcion == "2":
    try:
        busqueda_rut = input("Ingrese el RUT a buscar: ")
        if busqueda_rut == "":
            raise ValueError("El RUT no puede estar vacío.")

        encontrado = False
        for af in datosclientes:
            if af["rut"] == busqueda_rut:
                print("Afiliado encontrado:")
                print("Nombre:", af["nombre"])
                print("Apellido:", af["apellido"])
                print("Edad:", af["edad"])
                print("Estado civil:", af["estado_civil"])
                print("Género:", af["genero"])
                print("Fecha de afiliación:", af["fecha_afiliacion"])
                encontrado = True
                break
        if not encontrado:
            print("Afiliado no encontrado.")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
        



    



