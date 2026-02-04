#num = input() # captura de String o char
#print('Hola')
#print("Mundo")

numero = int(input())
base = int(input())
nueva_base = int(input())
resultado = []
division = 1
while division >= 0:
    if base == 10:
        division = numero // nueva_base
        resto = numero % nueva_base
        resultado.append(resto)



'''
print(numero+1) 
print(num+1)'''