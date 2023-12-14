def keliling_luas(x,y,z):
    maksimal = max([x,y,z])
    if maksimal == x:
        panjang_1, panjang_2 = y,z
    elif maksimal == y:
        panjang_1, panjang_2 = x,z
    else:
        panjang_1, panjang_2 = x,y
        
    if x==y==z:
        print("Segitigamu sama sisi!")
        keliling = z*3
        luas = 1/2*x*(3/4*(x**2))**1/2
    elif maksimal**2 == panjang_1**2+panjang_2**2:
        print("Segitigamu siku-siku!")
        keliling = maksimal + panjang_1 + panjang_2
        luas = 1/2*panjang_1*panjang_2
    elif x==y or y==z or x==z:
        if x==y:
            sisi = x
            alas = z
        elif y==z:
            sisi = y
            alas = x
        else: 
            sisi = z
            alas = y
        print("segitigamu sama kaki!")
        keliling = 2*sisi + alas
        luas = 1/2*alas*((sisi**2)*1/4*(alas)**2)**1/2
    else:
        print("segitigamu sakkarep")
        keliling = maksimal+panjang_1+panjang_2
        luas = print("ndak tahu malas")
    return keliling, luas   

print(keliling_luas(3,4,5))     