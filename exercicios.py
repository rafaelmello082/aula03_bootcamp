### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
"""reg_qtd = input("Todos os registros de quantidade são positivos (s/n)? ")
reg_prc = input("Todos os registros de preço são positivos (s/n)? ")

if (reg_qtd == 's' or reg_qtd == "S") and (reg_prc == 's' or reg_prc == "S"):
  print("Dados válidos!")
else:
  print("Dados inválidos...")"""

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
"""print("\033c", end="")
dado_sensor = input("Diga o status da leitura do sensor ((B)aixa, (M)édia ou (A)lta): ")
if dado_sensor.lower() == 'b' or dado_sensor.lower() == 'baixa':
  print('Leitura do sensor é baixa!')
elif dado_sensor.lower() == 'm' or dado_sensor.lower() == 'media' or dado_sensor.lower() == 'média':
  print('Leitura do sensor é média!')
elif dado_sensor.lower() == 'a' or dado_sensor.lower() == 'alta':
  print('Leitura do sensor é alta!')
else:
  print('Alternativa inválida!')"""

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""print("\033c", end="")
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

for item in log.values():
  if item.lower() == 'error':
    print('A severidade do sistema é alta!')
    break"""

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""print("\033c", end="")
idade_errada = True
email_errado = True

while idade_errada:
  try:
    idade = int(input('Digite sua idade: '))
    if (idade < 18 or idade > 65):
      print('A idade deve estar entre 18 e 65 anos!')
    else:
      idade_errada = False
  except ValueError:
    print('Você não digitou um número inteiro!')
  
while email_errado:
  email = input('Digite seu email: ')
  if '@' not in email:
    print('Email inválido!')
  else:
    email_errado = False
    
print('\nDados inseridos com sucesso!')"""

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
"""print("\033c", end="")
transacao = {'valor': 12000, 'hora': 20}
for key, value in transacao.items():
  if (key == 'valor' and value > 10000) or (key == 'hora' and (value < 9 or value > 18)):
    print(f'Transação é suspeita')
    break"""

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""print("\033c", end="")
texto = 'hoje e nossa segunda aula do bootcamp, bootcamp de python python'
texto_lista = texto.split(' ')
contagem = {}

for palavra in texto_lista:
  palavra = "".join(char for char in palavra if char.isalpha())
  if palavra in contagem:
    contagem[palavra] += 1
  else:
    contagem[palavra] = 1
print(contagem)"""

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""print("\033c", end="")
lista_original = [10,20,30,40,50]
lista_normalizada = []

for item in lista_original:
  lista_normalizada.append((item - lista_original[0])/(lista_original[-1] - lista_original[0]))

print(lista_normalizada)"""

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
"""print("\033c", end="")
pessoas = [
{"nome": 'Ultra', "idade": 43}, 
{"nome": 'Porco', "idade": 43}, 
{"nome": 'Arruda', "idade": None}, 
{"nome": 'Luisinho', "idade": 42}, 
{"nome": 'Tabata', "idade": 38}, 
{"nome": 'Marina', "idade": 40}, 
{"nome": 'Livia', "idade": 11}, 
{"nome": 'Luisa', "idade": 2}, 
{"nome": 'Leticia', "idade": 1}
]

pessoas_final = []

for i in range(len(pessoas)):
  if pessoas[i]['nome'] != None and pessoas[i]['idade'] != None:
    pessoas_final.append(pessoas[i])

print(pessoas_final)"""

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
"""print("\033c", end="")
num_pares = []
for num in range(1,21):
  if num % 2 == 0:
    num_pares.append(num)
print(num_pares)"""

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""print("\033c", end="")
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_eletronicos = int(input('Digite o total de vendas de eletrônicos: '))
vendas_livros = int(input('Digite o total de vendas de livros: '))

total_eletronicos = 0
total_livros = 0

for item in vendas:
  if item['categoria'] == "eletrônicos":
    total_eletronicos += item['valor'] * vendas_eletronicos
  if item['categoria'] == "livros":
    total_livros += item['valor'] * vendas_livros

print(f'Total de eletrônicos: {total_eletronicos}')
print(f'Total de livros: {total_livros}')"""

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
"""print("\033c", end="")
dado = input('Digite o dado a ser inserido e tecle ENTER. Para finalizar o programa, digite "sair". ')
while dado.lower() != 'sair':
  dado = input('Digite o dado a ser inserido e tecle ENTER. Para finalizar o programa, digite "sair". ')
print('Até a próxima!')"""

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
"""print("\033c", end="")
num = -1
while num not in range(0,6):
  num = int(input('Digite um número entre 0 e 5: '))
print('Parabéns! Até a próxima!')"""

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
"""print("\033c", end="")
pag_atual = int(input("Digite a página atual: "))
pag_totais = int(input("Digite a quantidade total de páginas: "))

while pag_atual >= pag_totais:
  pag_atual = int(input('\nErro: valor deve ser menor que o da quantidade total de páginas!\nDigite novamente a página atual: '))
  pag_totais = int(input("Digite a quantidade total de páginas: "))
while pag_atual < pag_totais:
  print(f'Processando página {pag_atual} de um total de {pag_totais} páginas...')
  pag_atual += 1

print('Paginação concluída. Até a próxima!')"""

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
print("\033c", end="")
num_tentativas = int(input("Digite o número de tentativas: "))
max_tentativas = int(input("Digite a quantidade máxima de tentativas: "))

while num_tentativas >= max_tentativas:
  num_tentativas = int(input('\nErro: valor deve ser menor que o da quantidade máxima de tentativas!\nDigite novamente o número de tentativas: '))
  max_tentativas = int(input("Digite a quantidade máxima de tentativas: "))
while num_tentativas < max_tentativas:
  print(f'Processando {num_tentativas}a tentativa de um total de {max_tentativas} tentativas...')
  num_tentativas += 1

print('Você alcançou o número máximo de tentativas. Até a próxima!')


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
"""print("\033c", end="")
try:
  valor = int(input('Digite um número inteiro diferente de zero: '))
  while valor != 0:
    valor = int(input('Digite um número inteiro diferente de zero: '))
  print('Você digitou o número zero...')
except:
  print('Você não digitou um número inteiro...')
finally:
  print('Fim do programa. Até a próxima!')"""
