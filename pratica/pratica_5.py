class musica:
    nome = ''
    artista = ''
    duracao = ''
    
musica_relax = musica()
musica_relax.nome = 'Thunderstruck'
musica_relax.artista = 'AC/DC'
musica_relax.duracao = '4:53'

musica_top = musica()
musica_top.nome = 'Back in Black'
musica_top.artista = 'AC/DC'
musica_top.duracao = '4:14'

musica_massa = musica()
musica_massa.nome = 'Moneytalks'
musica_massa.artista = 'AC/DC'
musica_massa.duracao = '3:46'

print(f'Musica: {musica_relax.nome}')