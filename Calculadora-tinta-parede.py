while True:
    largura = float(input('Qual a largura da parede? '))
    altura = float(input('Qual a altura da parede? '))
    area = largura * altura
    litro = area / 2

    print('A sua area total é de {}m²' .format(area))
    print('Para pintar a area total da parede voce precisa de {} litros de tinta' .format(litro))
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break