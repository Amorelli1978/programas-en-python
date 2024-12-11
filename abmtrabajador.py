import os
# Crear el diccionario para almacenar los datos del trabajador
trabajador = {
    'dni': '',
    'nombre_apellido': '',
    'año_de_ingreso': '',
    'sexo': '',
    'edad': '',
    'salario': ''
}

# Lista vacía para almacenar los datos de los trabajadores
lista_trabajadores = []



# --------------------------  Función Buscar dni 
def buscar_dni(dni_buscado):
    for indice, trabajador in enumerate(lista_trabajadores):
        if trabajador['dni'] == dni_buscado:
            return True, indice, trabajador
    return False, None


# --------------------------  Función Validar año de ingreso
def validar_anio():
    while True:           
            entrada = input("Año de ingreso    :")  
            try:
                # Intentar convertir la entrada a un número entero
                anio = int(entrada)
                return anio
            except ValueError:
                print("\033[33mPor favor, ingrese una edad válida.\033[0m") 


# --------------------------  Función Validar entero
def validar_edad():
    while True:           
            entrada = input("Edad              :")  
            try:
                # Intentar convertir la entrada a un número entero
                edad = int(entrada)
                return edad
            except ValueError:
                print("\033[33mPor favor, ingrese una edad válida.\033[0m") 


# --------------------------- Funcion Validar sexo
def validar_sexo():
    while True:          
            entrada= input("Sexo (F/M)        : ").upper()
            if entrada in ['F','M']:
                return entrada
            else:
                print("\033[33mEl sexo debe ser F o M\033[0m")


def validar_salario():
        while True:         
            entrada= input("salario           : ")
            try:
                # intentar convertir entrada a numero flotante
                salario = float(entrada)
                return salario
            except:
                print("\033[33mPor favor, ingrese un salario válido.\033[0m")  


# --------------------------  Función Registrar   
def registrar_trabajadores():
    global trabajador
    while True:
        os.system("cls")
        print("\n\n\033[32m** MÓDULO REGISTRO DE TRABAJADORES **\033[0m\n")
        dni_a_buscar = input("Ingrese el dni o '\033[33m000\033[0m' para volver al Menú: ")
        if dni_a_buscar == '000':
            break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar)
            if resultado_busqueda[0]:
                print(f"\nDNI \033[32m{dni_a_buscar}\033[0m ya registrado!!")
                trabajador = resultado_busqueda[2] 
                input(f"\nPertenece al trabajador: {trabajador['nombre_apellido']}") 
                continue    
            else:
                trabajador['dni'] = dni_a_buscar
                trabajador['nombre_apellido'] = input("Nombre y apellido : ").lower().title()    
                trabajador['año_de_ingreso'] = validar_anio()
                trabajador['sexo'] = validar_sexo()
                trabajador['edad'] = validar_edad()
                trabajador['salario'] = validar_salario()
                lista_trabajadores.append(trabajador.copy())
                input("\nTrabajador Registrado, presione <enter>")


def listar_trabajadores():
    os.system("cls")
    print("\n\033[32m              ** REPORTE DE TRABAJADORES **\n")
    print("Nro    DNI         NOMBRE                        AÑO INGRESO       SEXO     EDAD    SALARIO ")
    print("===    ===         ======                        ===========       ====     ====    =======\033[0m")
    
    acumula_salario=0
    for contador,trabajador in enumerate(lista_trabajadores,1):
        print(f"{contador:<7}{trabajador["dni"]:<12}{trabajador["nombre_apellido"]:<32}"
              f"{trabajador["año_de_ingreso"]:<17}{trabajador["sexo"]:<9}{trabajador["edad"]:<8}"
              f"{trabajador["salario"]}")
        acumula_salario+=trabajador["salario"]
        
    salario_promedio= acumula_salario / len(lista_trabajadores)
    print("--------------".rjust(66))
    print("Salario Promedio: ".rjust(41),end="")
    print(f"\033[32m{salario_promedio:>24}\033[0m")
    
    input("Presione una tecla para continuar...")


def consultar_trabajadores():
    global trabajador
    while True:
        os.system("cls")
        print("\n\n\033[32m** MÓDULO CONSULTA DE TRABAJADORES **\033[0m\n")
        dni_a_buscar = input("Ingrese el dni o '\033[33m000\033[0m' para volver al Menú: ")
        if dni_a_buscar == '000':
            break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar)
            if resultado_busqueda[0]:
                print(f"\nDNI \033[32m{dni_a_buscar}\033[0m ya registrado!!")
                trabajador = resultado_busqueda[2]
                
                print("DNI            : ",trabajador["dni"])
                print("NOMBRE         : ",trabajador["nombre_apellido"])
                print("AÑO DE INGRESO : ",trabajador["año_de_ingreso"])
                print("SEXO           : ",trabajador["sexo"])
                print("EDAD           : ",trabajador["edad"])
                print("SALARIO        : ",trabajador["salario"])
            else:
                print(f"\nDNI = \033[32m{dni_a_buscar}\033[0m, no esta registrado!!.")
                
            input("\n\nIngrese una tecla para continuar...")
# -----------------------------Funcion eliminar trabajador
def eliminar_trabajadores():
    while True:
        os.system("cls")
        print("\n\n   \033[32m** MODULO DE ELIMINACION **\033[0M")
        #print("\n\nIngrese el DNI del trabajador a consultar o \033[33m000\033[0m para retornar al menu:  ")
        dni_a_buscar=input("\nIngrese DNI de trabajadores O \033[32m 000\032[0m para retornar al menu: ")
        if dni_a_buscar=="000": break
        else:
            resultado_busqueda= buscar_dni(dni_a_buscar)
            if resultado_busqueda[0]==True:
                trabajador =resultado_busqueda[2]
                respuesta=input(f"Desea eliminar a {trabajador["nombre_apellido"]} S/N: ")
                if respuesta.upper() == "s":
                    indice= resultado_busqueda[1]
                    del lista_trabajadores[indice]
                    input("\nTrabajador eliminado, presione <ENTER>")
                else:
                    input(f"\nDNI \033[32m{dni_a_buscar}\033[0m , no registrado, presione <ENTER>")      

# --------------------------  Función Menu 
def main():
    while True:
        os.system("cls")
        print("\n\n\033[32m     *MENÚ DE OPCIONES*\033[0m")
        print("                     Opción".rjust(33))
        print("                     ------".rjust(33))
        print("Registrar trabajador ....... 1")
        print("Consultar trabajador ....... 2")
        print("Eliminar trabajador  ....... 3")
        print("Listar trabajadores  ....... 4")
        print("\033[33mSalir  ....... 0 \033[0m".rjust(40))
        while True:
            opcion = input("\033[32mOpción? \033[0m ".rjust(32))
            if opcion  in ['0','1','2','3','4']:
                break
            else:
                print("Opción inválida"); 
        
        if   opcion == '1': registrar_trabajadores() 
        elif opcion == '2': consultar_trabajadores()
        elif opcion == '3': eliminar_trabajadores()
        elif opcion == '4': listar_trabajadores()
        elif opcion == '0': break


# Cuerpo principal del programa
if __name__=="__main__":
    main()
