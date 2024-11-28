'''
num = input('Digite um número: ')

convert_num = int(num)


if convert_num % 2 == 0:
    print('PAR!')
else:
    print('IMPAR!')

input('Pressione ENTER para a parte 2')

idade = input('Digite sua idade: ')

if idade <= '12':
    print('Criança')
elif idade >= '13' and idade <= '18':
    print('Adolescente')
elif idade > '18':
    print('Adulto')

input('Pressione ENTER para parte 3')

user_aut = 'tuts'
senha_aut = '1234'

user = input('Digite o seu usuário: ')
senha = input('Digite sua senha: ')

if user != user_aut or senha != senha_aut:
    print('Credenciais invalidas')
else:
    print('Login efetuado com sucesso')

'''

x = input('Digite as cordenadas X: ')
y = input('Digite as cordenadas Y: ')

cord_x = int(x)
cord_y = int(y)

if cord_x > 0 and cord_y > 0:
    print("Primeiro Quadrante")
elif cord_x <= 0 and cord_y > 0:
    print("Segundo Quadrante")
elif cord_x <= 0 and cord_y <= 0:
    print("Terceiro Quadrante")
elif cord_x > 0 and cord_y <= 0:
    print("Quarto Quadrante")
else:
    print('O ponto está localizado no exio ou origem')