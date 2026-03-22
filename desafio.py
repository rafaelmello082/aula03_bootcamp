print("\033c", end="")
nome_errado = True
salario_errado = True
perc_errado = True

try:

  while nome_errado:
    try:
      nome = input('Digite seu nome: ')
      nome = nome.strip()
      nome_sem_traco_ponto = nome.lstrip('-').replace('.','')
      if nome.isnumeric() or nome_sem_traco_ponto.isnumeric():
        raise ValueError("Você digitou um número...\n")
      elif nome == '':
        raise ValueError("Você não digitou nada...\n")
      else:
        nome_errado = False
    except ValueError as e:
      print(e)
    
  while salario_errado:
    salario = input('Digite seu salário: ')
    try:
      salario = float(salario)
      if float(salario) < 0:
        print("O salário digitado não pode ser negativo...\n")
      elif isinstance(salario, float) == False:
        pass
      else:
        salario_errado = False
    except ValueError:
      print("O salário digitado não é um número válido...\n")

  while perc_errado:
    perc = input('Digite o percentual: ')
    try:
      perc = float(perc)
      if perc < 0:
        print("O percentual digitado não pode ser negativo...\n")
      elif isinstance(perc, float) == False:
        pass
      else:
        perc_errado = False
    except ValueError:
      print("O percentual digitado não é um número válido...\n")

  bonus = 1000 + salario * ((perc/100) + 1)
  print(f'\nOlá {nome}!\nSeu salário atual: {salario}\nSeu bônus: {bonus:.2f}')

except KeyboardInterrupt:
  print("\nVocê saiu do programa.")
finally:
  print('Até a próxima!')