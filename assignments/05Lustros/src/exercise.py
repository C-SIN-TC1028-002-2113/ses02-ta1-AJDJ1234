def main():
    #escribe tu código abajo de esta línea
    naci = input("Dame el año de nacimiento: ")
    año = input("Dame el año actual: ")
    lustros = (int(año) - int(naci))/ 5

    print("Los lustros que has vivido son:",lustros)

if __name__ == '__main__':
    main()
