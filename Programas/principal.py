import os  # Importa el módulo 'os' para ejecutar comandos del sistema operativo.

# Función para ejecutar 'reportbd.py'
def ejecutar_programa1():
    os.system('python reportbd.py')  # Ejecuta el archivo 'reportbd.py' usando Python.

# Función para ejecutar 'espirinet.py'
def ejecutar_programa2():
    os.system('python espirinet.py')  # Ejecuta el archivo 'espirinet.py'.

# Función para ejecutar 'conversorCSV1.py'
def ejecutar_programa3():
    os.system('python conversorCSV1.py')  # Ejecuta el archivo 'conversorCSV1.py'.

# Función para ejecutar 'comparar_xlsx.py'
def ejecutar_programa4():
    os.system('python comparar_xlsx.py')  # Ejecuta el archivo 'comparar_xlsx.py'.

# Función para ejecutar 'creacion.py'
def ejecutar_programa5():
    os.system('python creacion.py')  # Ejecuta el archivo 'creacion.py'.

# Función para ejecutar 'comparar2_xlsx.py'
def ejecutar_programa6():
    os.system('python comparar2_xlsx.py')  # Ejecuta el archivo 'comparar2_xlsx.py'.

# Función para ejecutar 'conversorCSV2.py'
def ejecutar_programa7():
    os.system('python conversorCSV2.py')  # Ejecuta el archivo 'conversorCSV2.py'.

# Función para ejecutar 'error_succion.py'
def ejecutar_programa8():
    os.system('python error_succion.py')  # Ejecuta el archivo 'error_succion.py'.

# Función para ejecutar 'Smtp_ofigrafic.py'
def ejecutar_programa9():
    os.system('python Smtp_ofigrafic.py')  # Ejecuta el archivo 'Smtp_ofigrafic.py'.

# Función para realizar la ejecución automática de los programas en un orden predeterminado.
def ejecucion_automatica():
    print("Ejecución automática de los programas en orden especificado.")  # Mensaje informativo.
    ejecutar_programa1()  # Ejecuta el primer programa.
    ejecutar_programa2()  # Ejecuta el segundo programa.
    ejecutar_programa3()  # Ejecuta el tercer programa.
    ejecutar_programa4()  # Ejecuta el cuarto programa.
    ejecutar_programa5()  # Ejecuta el quinto programa.
    ejecutar_programa6()  # Ejecuta el sexto programa.
    ejecutar_programa7()  # Ejecuta el séptimo programa.
    ejecutar_programa8()  # Ejecuta el octavo programa.
    ejecutar_programa9()  # Ejecuta el noveno programa.
    print("Ejecución automática completada.")  # Indica que la ejecución automática ha terminado.

# Función para mostrar un menú manual que permite ejecutar programas individuales.
def menu_manual():
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir.
        print("\nMenú Manual:")  # Título del menú.
        print("1. Ejecutar reportbd.py")  # Opción 1.
        print("2. Ejecutar espirinet.py")  # Opción 2.
        print("3. Ejecutar conversorCSV1.py")  # Opción 3.
        print("4. Ejecutar comparar_xlsx.py")  # Opción 4.
        print("5. Ejecutar creacion.py")  # Opción 5.
        print("6. Ejecutar comparar2_xlsx.py")  # Opción 6.
        print("7. Ejecutar conversorCSV2.py")  # Opción 7.
        print("8. Ejecutar error_succion.py")  # Opción 8.
        print("9. Ejecutar Smtp_ofigrafic.py")  # Opción 9.
        print("10. Volver al menú principal")  # Opción para volver al menú principal.

        opcion = input("Selecciona una opción: ")  # Solicita al usuario que elija una opción.

        if opcion == '1':  # Ejecuta 'reportbd.py' si se selecciona la opción 1.
            ejecutar_programa1()
        elif opcion == '2':  # Ejecuta 'espirinet.py' si se selecciona la opción 2.
            ejecutar_programa2()
        elif opcion == '3':  # Ejecuta 'conversorCSV1.py' si se selecciona la opción 3.
            ejecutar_programa3()
        elif opcion == '4':  # Ejecuta 'comparar_xlsx.py' si se selecciona la opción 4.
            ejecutar_programa4()
        elif opcion == '5':  # Ejecuta 'creacion.py' si se selecciona la opción 5.
            ejecutar_programa5()
        elif opcion == '6':  # Ejecuta 'comparar2_xlsx.py' si se selecciona la opción 6.
            ejecutar_programa6()
        elif opcion == '7':  # Ejecuta 'conversorCSV2.py' si se selecciona la opción 7.
            ejecutar_programa7()
        elif opcion == '8':  # Ejecuta 'error_succion.py' si se selecciona la opción 8.
            ejecutar_programa8()
        elif opcion == '9':  # Ejecuta 'Smtp_ofigrafic.py' si se selecciona la opción 9.
            ejecutar_programa8()
        elif opcion == '10' or 'q':  # Vuelve al menú principal si se selecciona la opción 10 o 'q'.
            break
        else:
            print("Opción no válida, por favor selecciona una opción del 1 al 10.")  # Mensaje de error.

# Función principal que muestra el menú principal al usuario.
def menu_principal():
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir.
        print("\nMenú Principal:")  # Título del menú.
        print("1. Ejecución automática de los programas en orden")  # Opción para ejecución automática.
        print("2. Menú manual para ejecutar cada programa")  # Opción para abrir el menú manual.
        print("3. Salir")  # Opción para salir del programa.

        opcion = input("Selecciona una opción: ")  # Solicita al usuario que elija una opción.

        if opcion == '1':  # Llama a la función de ejecución automática.
            ejecucion_automatica()
        elif opcion == '2':  # Llama a la función de menú manual.
            menu_manual()
        elif opcion == '3' or 'q':  # Sale del programa si se selecciona la opción 3 o 'q'.
            print("Saliendo del programa.")  # Mensaje de despedida.
            break
        else:
            print("Opción no válida, por favor selecciona una opción del 1 al 3.")  # Mensaje de error.

# Punto de entrada principal del programa.
if __name__ == '__main__':
    menu_principal()  # Llama al menú principal.
