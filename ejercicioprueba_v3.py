datosclientes = {"rut" : [],
                 "nombre" : [],
                 "apellido_paterno": [],           
                 "edad" : [],
                 "estado_civil" : [],
                 "genero": [],
                 "fecha_afiliacion": []}

print('Bienvenido al registro de Vida y Salud 💊🏥')
print()
while True:
    try:
        print('''  \nMenú de registo:
                    Opción [1].- Grabar (Registrar datos)
                    Opción [2].- Buscar (Filtrar por rut)
                    Opción [3].- Imprimir Certificados (Costo entre $1.000 y $1.500)
                    Opción [4].- Salir del programa''')
        opcion= int(input('\nIngrese un número del menú: '))
        while opcion not in [1,2,3,4]:
            print('Opción incorrecta. Sólo se puede del 1 al 4.')
            opcion= int(input('\nIngrese un número del menú: '))
        if opcion==1:
            print('\nAhora necesita completar los siguientes datos: ')
            while True:
                rut2 = input('\nIngrese su rut, sin puntos y sin guión: ')
                length = len(rut2)
                if length in [9,10]:
                    print("\nRUT aceptado.")
                    datosclientes["rut"].append(rut2)
                    break
                else:
                    print('Rut incorrecto, debe ingresar al menos 8 o máximo 9 caracteres.')
            while True:
                nombre2= input('\nIngrese su nombre SIN APELLIDO: \n')
                r1=int(input(f'\nEl nombre ingresado es {nombre2}.\nConfirme presionando [1] si no aprete cualquier tecla: '))
                if r1==1:
                    datosclientes["nombre"].append(nombre2)
                    break
            while True:
                try:
                    edad2 = int(input('\nIngrese su edad: '))
                    while edad2<18:
                        print('\nNO PUEDES SER MENOR DE EDAD. VUELVA A INTENTAR.\n')
                        edad2 = int(input('Ingrese su edad: '))
                    datosclientes["edad"].append(edad2)
                    break
                except ValueError:
                    print('\nDato incorrecto, debe ingresar sólo números.\n')
            while True:
                apellido2= input('\nIngrese su apellido paterno: \n')
                r2=int(input(f'\nEl apellido ingresado es {apellido2}.\nConfirme presionando [1] si no aprete cualquier tecla: '))
                if r2==1:
                    datosclientes["apellido_paterno"].append(apellido2)
                    break
            while True:
                try:
                    genero2= int(input('''Indique su género: 
                        [1] Masculino.
                        [2] Femenino.
                        [3] No-binario.
                        [4] Otro.'''))
                    match genero2:
                        case 1:
                            genero2 = 'Masculino'
                            datosclientes["genero"].append(genero2)
                            break
                        case 2:
                            genero2= 'Femenino'
                            datosclientes["genero"].append(genero2)
                            break
                        case 3:
                            genero2= 'No binario'
                            datosclientes["genero"].append(genero2)
                            break
                        case 4:
                            while True:
                                try:
                                    genero2= input('Indique su género: ')
                                    r3= int(input(f'Usted ingresó {genero2}.Confirme presionando [1] si no aprete cualquier tecla: '))
                                    if r3==1:
                                        datosclientes["genero"].append(genero2)
                                        break
                                except ValueError:
                                    print('\nDato incorrecto, debe ingresar sólo números.\n')
                        case _:
                            print('No existe la opción.')
                except ValueError:
                    print('\nDato incorrecto, debe ingresar sólo números.\n')
            while True:
                try:
                    estado_civil2=int(input('''Ingrese su estados civil:
                        [1] Casado.
                        [2] Soltero.
                        [3] Viudo.'''))
                    match estado_civil2:
                        case 1:
                            estado_civil2= 'C'
                            datosclientes["estado_civil"].append(estado_civil2)
                            break
                        case 2:
                            estado_civil2= 'S'
                            datosclientes["estado_civil"].append(estado_civil2)
                            break
                        case 3:
                            estado_civil2= 'V'
                            datosclientes["estado_civil"].append(estado_civil2)
                            break
                        case _:
                            print('No existe esa opción.')
                except ValueError:
                    print('\nDato incorrecto, debe ingresar sólo números.\n')
            while True:
                try:
                    fecha_afiliacion2_dia = int(input('Ingrese el día de ingreso en números DD: '))
                    if not 1 <= fecha_afiliacion2_dia <= 31:
                        print("Día inválido. Debe estar entre 1 y 31.")
                        continue
                    if len(str(fecha_afiliacion2_dia)) == 1:
                        fecha_afiliacion2_dia = '0' + str(fecha_afiliacion2_dia)
                    else:
                        fecha_afiliacion2_dia = str(fecha_afiliacion2_dia)
                    fecha_afiliacion2_mes = int(input('Ingrese el mes de ingreso en números MM: '))
                    if not 1 <= fecha_afiliacion2_mes <= 12:
                        print("Mes inválido. Debe estar entre 1 y 12.")
                        continue
                    if len(str(fecha_afiliacion2_mes)) == 1:
                        fecha_afiliacion2_mes = '0' + str(fecha_afiliacion2_mes)
                    else:
                        fecha_afiliacion2_mes = str(fecha_afiliacion2_mes)
                    fecha_afiliacion2_anno = int(input('Ingrese el año de ingreso en números AAAA: '))
                    if len(str(fecha_afiliacion2_anno)) != 4:
                        print("Año inválido. Debe tener 4 dígitos.")
                        continue
                    fecha_afiliacion2_anno = str(fecha_afiliacion2_anno)
                    break
                except ValueError:
                    print('\nDato incorrecto, debe ingresar sólo números.\n')
            fecha_afiliacion2 = f'{fecha_afiliacion2_dia}/{fecha_afiliacion2_mes}/{fecha_afiliacion2_anno}'
            datosclientes["fecha_afiliacion"].append(fecha_afiliacion2)
        
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
                print("\nRUT no encontrado.\n")

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
            print("Versión del programa 3.0")
            break

    except ValueError:
        print('\nDato incorrecto, debe ingresar sólo números.\n')
    except Exception as e:
        print(f'Error inesperado: {e}\n')