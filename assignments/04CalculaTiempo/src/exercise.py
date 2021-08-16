def main():
    #escribe tu código abajo de esta línea
    edad = input("Dame tu edad: ")
    año = input("Dame el año actual: ")
    añofinal = (100-int(edad)) + int(año) 

    print("Cumplirás 100 años en el año:",añofinal)

if __name__ == '__main__':
    main()
