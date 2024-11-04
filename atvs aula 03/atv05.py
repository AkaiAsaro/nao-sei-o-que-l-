num1 = int((input('digite um numero: ')))
num2 = int((input('digite um numero: ')))
num3 = int((input('digite um numero: ')))
num4 = int((input('digite um numero: ')))

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
if num4 > maior:
  maior = num4
if num4 < menor:
  menor = num4

soma = maior + menor

print(f'o maior é: {maior}')
print(f'o menor é: {menor}')
print(f'a soma dos dois números é: {soma}')

