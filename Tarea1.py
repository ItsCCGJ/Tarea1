if __name__ == "__main__":
    print("Lista de Supermercado")
    lista_sm={}

    archivo = open("supermercado.txt","r").read().split('\n')
    for linea in archivo:
        if linea in lista_sm.keys():
            lista_sm[linea]+=1
        else:
            lista_sm[linea]=1
    print(lista_sm)

    for i in range(3):
        articulo = input("Introduzca un articulo a su lista de supermercado: ")
        if articulo in lista_sm.keys():
            lista_sm[articulo]+=1
        else:
            lista_sm[articulo]=1

    print("-----------")
    print("Lista actual")
    print("-----------")
    for k,v in lista_sm.items():
        print(k,v)

    cont = input("\n Desea eliminar un articulo? (s/n): ")
    while cont.lower()=="y":
        opc = input("\n Ingrese el articulo que quiere eliminar: ")
        if opc in lista_sm.keys():
            lista_sm[opc]-=1
            print("Se elimino "+opc+".")
            if lista_sm[opc]==0:
                del lista_sm[opc]
                print("El articulo "+opc+"fue eliminado exitosamente")
                cont = input("\nDesea eliminar otro articulo? (s/n): ")
            else:
                print("Articulo invalido, intente otra vez")

    for k,v in lista_sm.items():
        print(k,v)

        cont = input("\nDesea sustituir un articulo? (s/n): ")
        while cont.lower()=="y":
            opc = input("\nIngrese el articulo a sustituir: ")
            if opc in lista_sm.keys():
                print("Se sustituyo"+opc+".")
                del lista_sm[opc]
                cont="n"
            else:
                print("Articulo invalido, intente otra vez")
            sub = input("Por cual articulo sustituira el "+opc+"?")
            if sub in lista_sm:
                lista_sm[sub]+=1
                print("+1 "+sub)
            else:
                lista_sm[sub]=1
                print("Nuevo articulo agregado")

            print("---------------")
            print("Lista actual")
            print("---------------")
            for k,v in lista_sm.items():
                print(k,v)

            archivo = open("supermercado.txt","a+")
            for e in lista_sm:
                archivo.write("\n+e")
            archivo.close()
