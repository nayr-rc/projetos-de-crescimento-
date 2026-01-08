l1 = (int(input('Digite o primeiro lado do triângulo: ')))
l2 = (int(input('Digite o segundo lado do triângulo: ')))
l3 = (int(input('Digite o terceiro lado do triângulo: ')))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados acima PODEM FORMAR um triângulo ', end='')
else:
    print('Os lados acima NÃO PODEM FORMAR um triângulo')
    exit()

if l1 == l2 == l3:
        print('EQUILÁTERO!')
elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
else:
        print('ISÓSCELES!')