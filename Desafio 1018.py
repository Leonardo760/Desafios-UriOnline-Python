X = int(input())
if  0 < X < 1000000:
    cem = X / 100.00
    um = X%100
    cinquenta = um  / 50.00
    um = um%50
    vinte = um / 20.00
    um = um%20
    dez = um / 10.00
    um = um%10
    cinco = um / 5.00
    um = um % 5
    dois = um / 2.00
    um = um%2
    um = um / 1.00
    print("%i" % X)
    print("%i nota(s) de R$ 100,00" % cem)
    print("%i nota(s) de R$ 50,00" % cinquenta)
    print("%i nota(s) de R$ 20,00" % vinte)
    print("%i nota(s) de R$ 10,00" % dez)
    print("%i nota(s) de R$ 5,00" % cinco)
    print("%i nota(s) de R$ 2,00" % dois)
    print("%i nota(s) de R$ 1,00" % um)