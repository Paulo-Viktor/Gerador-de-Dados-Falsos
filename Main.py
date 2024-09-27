from Funções import *

titulos('Gerador de Pessoa Falsa')

sleep(1)

while True:
    resp = menu_principal()

    if resp == '1':
        gerar_dados_completos()

    elif resp == '2':
        resp2 = menu_dados_especificos()
        gerar_dados_especificos(resp2)

    elif resp == '0':
        print('\nSaindo do programa...')
        sleep(1)
        break

    continuar = input('\nDeseja continuar? (S/N)\n-> ').upper()

    while continuar not in ['S', 'N']:
        continuar = input('ERRO! Por favor, digite S ou N para continuar.\n-> ').upper()

    if continuar == 'N':
        print('\nSaindo do programa...')
        sleep(1)
        break