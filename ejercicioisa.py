elif opcion == 2:
            rut_buscar = input("Ingrese el RUT a buscar: ")
            if rut_buscar in datosclientes["rut"]:
                idx = datosclientes["rut"].index(rut_buscar)
                print(f"\nInformación del afiliado:")
                print(f"RUT: {datosclientes['rut'][idx]}")
                print(f"Nombre: {datosclientes['nombre'][idx]}")
                print(f"Apellido: {datosclientes['apellido_paterno'][idx]}")
                print(f"Edad: {datosclientes['edad'][idx]}")
                print(f"Estado civil: {datosclientes['estado_civil'][idx]}")
                print(f"Género: {datosclientes['genero'][idx]}")
                print(f"Fecha de afiliación: {datosclientes['fecha_afiliacion'][idx]}\n")
            else:
                print("RUT no encontrado.\n")

        elif opcion == 3:
            if not datosclientes["rut"]:
                print("No hay registros aún.")
            else:
                print("\nCERTIFICADOS DISPONIBLES:")
                for i, rut in enumerate(datosclientes["rut"]):
                    print(f"{i+1}. {datosclientes['nombre'][i]} {datosclientes['apellido_paterno'][i]} - RUT: {rut} - Fecha afiliación: {datosclientes['fecha_afiliacion'][i]} - Certificado: ${1000 + (i * 100)}")
                print()

        elif opcion == 4:
            print("\nSaliendo del programa....")
            print("Desarrollado por Claudio Alvarez, Felipe Lagos, Luis Maraboli")
            print("Versión del programa 1.0")
            break