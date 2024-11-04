pedir_idade = int(input('digite sua idade: '))
if pedir_idade < 12:
  print('você é uma criança')
elif pedir_idade >= 12 and pedir_idade <=17:
  print('você é adolescente')
elif pedir_idade >= 18 and pedir_idade <= 59:
  print('você é adulto')
else: 
  print('você é idoso')
