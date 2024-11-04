num1 = int((input('digite um numero: ')))
num2 = int((input('digite um numero: ')))
num3 = int((input('digite um numero: ')))

maior = num1
menor = num1

if num2 > maior:
  maior = num2
if num2 < menor:
  menor = num2
if num3 > maior:
  maior = num3
if num3 < menor:
  menor = num3

print(f'o maior é: {maior}')
print(f'o menor é: {menor}')

