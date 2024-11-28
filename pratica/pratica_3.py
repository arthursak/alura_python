num = [1,2,3,4,5,6,7,8,9,10]
nome = ['Arthur','Murilo','Francine','Rocha']
ano = [1999,2024]

'''
for n in num:
    # Lista
    print(n)
    # Soma Impar
    if n%2 != 0:
        print(n + n)

# Lista reversa
for n in reversed(num):
    print (n)


# Tabuada
num_inicial = int(input('Digite um número: '))

for i in range(1,11):
    tabuada = num_inicial * i

    print(f'Tabuada do número {num_inicial}:\n{tabuada}')

'''

soma_num = 0


try:
    for n in num:
        soma_num += n
    print(soma_num)
    print(soma_num / len(num))

except TypeError as e:
    print(e)
except Exception as e:
    print(e)


