from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Monica', 6)
restaurante_mexicano.receber_avaliacao('José', 8)
restaurante_mexicano.receber_avaliacao('Ernesto', 2)
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('Oshin', 3)
restaurante_japones.receber_avaliacao('Okani', 10)
restaurante_japones.receber_avaliacao('Myotenchu', 7)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()