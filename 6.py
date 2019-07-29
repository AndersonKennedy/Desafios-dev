#Problema do quadrado gêmeo das partes 
# número de Kaprekar
numero = input('numero: ').strip()
is_Kaprekar = False
parte1 = parte2 = ''
for indice,digito in enumerate(numero):
    parte1,parte2 = parte1 + numero[indice:indice+1],numero[indice+1:]
    if parte2.isnumeric() and parte1.isnumeric():
        soma = (int(parte1)+int(parte2))
        if soma**2 == int(numero):
            print(1)
            is_Kaprekar = True
            break
if not is_Kaprekar:
    print(0)