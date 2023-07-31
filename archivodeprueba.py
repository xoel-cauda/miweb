def bits_a_num():
    print("En este transformador de numeros binarios a numeros enteros hay que ingresar los numeros")
    print("en un orden donde el primer numero ingresado sera el de la derecha y el ultimo el que esta")
    print("colocado a la izquierda")
    n=0
    cont=0
    bit=0
    w=True
    while True:
        bit=int(input("Ingrese el primer digito del num binario: "))
        if bit == 1 or bit == 0:
            break

    if bit == 1:
        n=1
    else:
        cont+=0
    while bit != -1:
        bit=int(input("Ingrese el sig digito del numero binario: "))
        if w==True and bit ==1:
            n+=2
            cont+=1
            w=False
        elif w==True and bit == 0:
            cont+=1
            w=False
        elif bit == -1:
            print(f"El numerito es:{n}")
            break
        elif bit== 1:
            for a in range(cont):
                n += (2 * 2)
                cont+=1
        elif bit==0:
            cont+=1
        else:
            while bit != 1 or bit != 0:
                bit=int(input("Ingrese un digito valido: "))

            
    print(f"El numero es:{n}")



bits_a_num()