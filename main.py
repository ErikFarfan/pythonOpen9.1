def main():
    ingresa=input('Ingresa los nombres de 5 paises que conozcas separados por coma : ')
    pais=set(ingresa.split(','))
    paises=sorted(pais)
    print(f'los paises que conoces son {paises[0]},{paises[1]},{paises[2]},{paises[3]},{paises[4]}')










if __name__=='__main__':
    main()