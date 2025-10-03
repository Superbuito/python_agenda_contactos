
def mostrar_menu():
    print("\nMenú de la Agenda de Contactos")
    print("1. Agregar contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contacto")
    print("5. salir del programa")
    print("-" * 30) 

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto:")
    telefono = input("Ingrese el número de teléfono del contacto:")
    email = input("Ingrese el correo electrónico del contacto:")
    agenda[nombre] = {"teléfono": telefono, "email": email}
    print(f"Contacto {nombre} agregado exitosamente.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar:" )
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado exitosamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")  

def listar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("Lista de contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {info['teléfono']}, Email: {info['email']}")
            print("-" * 30 )



def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar:")
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} ")
        print(f"Teléfono: {agenda[nombre]['teléfono']}")
        print(f"email: {agenda[nombre]['email']}") 
    else:
        print(f"El contacto {nombre} no existe en la agenda.")


def agenda_contactos():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Por favor eliga una opción:")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            break
        else:
            print("Por favor eliga una opción válida.")

agenda_contactos()

    