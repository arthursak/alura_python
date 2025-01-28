class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Tio Juca'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()
restaurante_pizza.nome = '4 Queijos'
restaurante_pizza.categoria = 'Pizza'
restaurante_pizza.ativo = False

restaurantes = [restaurante_praca,restaurante_pizza]

print(restaurantes)
print(vars(restaurante_praca))