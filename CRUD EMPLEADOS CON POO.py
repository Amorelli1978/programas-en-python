import os
from clases.mis_clases import Trabajador,GestionTrabajadores
from utility.validaciones import *

def main():
    gestor=GestionTrabajadores()
        
    while True:
        os.system("cls")
        print("\n\033[32m**MENU DE OPCIONES**\033[0m\n")
        print("1. Registrar Trabajador")
        print("2. Buscar Trabajador")
        print("3. Eliminar Trabajador")
        print("4. Listar Trabajador")
        print("0. Salir.....")
        while True:
            opcion = input("\033[32mOpción: \033[0m ".rjust(32))
            if opcion  in ['0','1','2','3','4']:
                break
            else:
                print("Opción inválida"); 

        if opcion == "1":
            dni= input("DNI: ")
            nombre_apellido= input("Nombre y Apellido: ").upper().title()
            anio_de_ingreso= input("Año de Ingreso: ")
            sexo= input("Sexo (F/M): ").upper
            edad= int(input("Edad: "))
            salario= float(input("Salario: "))

            #if (validar_dni(dni) and validar_nombre_apellido(nombre_apellido) and 
                #validar_anio_de_ingreso(anio_de_ingreso) and validar_sexo(sexo) and 
                #validar_edad(edad) and validar_salario(salario)):
            gestor.registrar_trabajador(dni,nombre_apellido,anio_de_ingreso,sexo,edad,salario)
            print("\n\033[32**Trabajador registrado con exito**\033\0m")
            #else:
                #print("\n\033[32mDatos Invalidos, ingrese los datos correctamente\033[0m")
            input("Ingrese una tecla para continuar")

        elif opcion=="2":
            dni=input("DNI: ")
            trabajador=gestor.buscar_trabajador(dni)
            if trabajador:
                print(trabajador)
            else:
                print("\nTrabajador no encontrado.")
            input("Ingrese una tecla para continuar.")
            
        elif opcion == "3":
            dni=input("DNI: ")  
            if gestor.eliminar_trabajadores(dni):
                print("Trabajador eliminado.")
            else:
                print("Trabajador no encontrado.")
            input("Ingrese una tecla para continuar.")
            
        elif opcion =="4":
            trabajadores =gestor.listar_trabajadores()
            for trabajador in trabajadores:
                print(trabajador)
            input("Ingrese una tecla para continuar.")
                
        elif opcion == "0":
            break
        else:
            print("Opcion no valida, ingrese una opcion correcta")
            
if __name__ == "__main__":
    main()