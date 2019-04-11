X = int(input())
horas = X / 3600
resto = X%3600
minutos = resto / 60
resto = resto%60
segundos = resto
print ("%i:%i:%i" %(horas, minutos, segundos,))