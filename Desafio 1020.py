X = int(input())
ano = X / 365
resto = X%365
mês = resto / 30
resto = resto%30
dias = resto
print ("%i ano(s)"%ano)
print ("%i mes(es)"%mês)
print ("%i dia(s)"%dias)
