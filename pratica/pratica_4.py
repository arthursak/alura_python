'''
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
lista = [{'nome':'Arthur','idade':'25','cidade':'Palhoça'}]
print(lista)

# 2 - Utilizando o dicionário criado no item 1:
# - Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

for info in lista:
    att_idade = input('Digite a idade: ')
    info['idade'] = att_idade

print(lista)

# - Adicione um campo de profissão para essa pessoa;
prof = input('Digite a profissão dessa pessa: ')
lista.append({'profissao': prof})

print(lista)
# - Remova um item do dicionário.
remover = input('O que você gostaria de remover? ')

dicionario = lista[0]

if remover in dicionario:
    del dicionario[remover]
    print(f"Campo {remover} removido com sucesso!")
    print(lista)
else:
    print("O campo especificado não existe no dicionário.")

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.


palavra = input('Digite uma palavra que deseja verificar: ')

dicionario = lista[0]

if palavra in dicionario:
    print('A palvra está no dicionario!')

else:
    print('Palavra não consta no dicionario')
'''

def contar_palavras(frase):
  
  palavras = frase.lower().split()

  # Cria um dicionário vazio para armazenar as contagens
  contagens = {}

  # Itera sobre cada palavra e incrementa a contagem no dicionário
  for palavra in palavras:
    if palavra in contagens:
      contagens[palavra] += 1
    else:
      contagens[palavra] = 1

  return contagens

# Pede ao usuário para digitar a frase
frase = 'pra eu eu teste teste teste'

# Chama a função para contar as palavras
resultado = contar_palavras(frase)

# Imprime o resultado
print(resultado)
