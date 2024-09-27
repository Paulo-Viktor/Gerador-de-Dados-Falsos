from faker import Faker
from rich import print
from time import sleep

fake = Faker('pt_BR')

def gerar_nome():
    nome = fake.name()

    nome_separado = nome.split(' ')

    primeiro_nome = nome_separado[0].replace('.', '')

    segundo_nome = nome_separado[1]

    if segundo_nome in ['da', 'de', 'do']:
        segundo_nome = nome_separado[2]

    print(f'[bold]NOME:[/bold] {nome}\n')

    return primeiro_nome, segundo_nome

def gerar_cpf():
    print(f'[bold]CPF:[/bold] {fake.cpf()}\n')

def gerar_email(primeiro_nome, segundo_nome):

    dominio = fake.free_email_domain()

    numero = fake.random_int(min=1, max=100)

    print(f'[bold]EMAIL:[/bold] {primeiro_nome}.{segundo_nome}{numero}@{dominio}\n')

def gerar_endereco():

    endereco = f'{fake.street_name()}, {fake.building_number()} - {fake.bairro()}, {fake.city()} - {fake.state_abbr()}, {fake.postcode()}'

    print(f'[bold]ENDEREÇO:[/bold] {endereco}\n')

def gerar_numero_tel():
    print(f'[bold]NÚMERO DE TELEFONE:[/bold] {fake.phone_number()}')

def gerar_dados_completos():
    subtitulos('Gerando dados')
    sleep(1)

    primeiro_nome, segundo_nome = gerar_nome()

    gerar_cpf()

    gerar_email(primeiro_nome, segundo_nome)

    gerar_endereco()

    gerar_numero_tel()

def gerar_dados_especificos(resp2):
    print()
    print('=-' * 35)

    if resp2 == '1':
        print('Gerando [bold]NOME[/bold] aleatório\n')
        sleep(1)
        print(f'Nome gerado: [bold]{fake.name()}[/bold]')

    elif resp2 == '2':
        print('Gerando [bold]CPF[/bold] aleatório\n')
        sleep(1)
        print(f'CPF gerado: [bold]{fake.cpf()}[/bold]')

    elif resp2 == '3':
        print('Gerando [bold]EMAIL[/bold] aleatório\n')
        sleep(1)
        print(f'Email gerado: [bold]{fake.free_email()}[/bold]')

    elif resp2 == '4':
        print('Gerando [bold]ENDEREÇO[/bold] aleatório\n')
        sleep(1)
        print(f'Endeeço gerado: [bold]{fake.street_name()}, {fake.building_number()} - {fake.bairro()}, {fake.city()} - {fake.state_abbr()}, {fake.postcode()}[/bold]')

    elif resp2 == '5':
        print('Gerando [bold]NÚMERO DE TELEFONE[/bold] aleatório\n')
        sleep(1)
        print(f'Número de telefone gerado: [bold]{fake.phone_number()}[/bold]')

    print('=-' * 35)

def titulos(msg):
    print('~' * 70)
    print(f'{msg}'.center(70).upper())
    print('~' * 70)

def subtitulos(msg):
    print('=-' * 35)
    print(f'{msg}'.center(70).upper())
    print('=-' * 35)

def menu_principal():
    print()
    subtitulos('Menu Principal')
    print('''Selecione uma ação com base em seu número de correspondência:
    
1 - Gerar dados completos

2 - Gerar dado específico
          
0 - Sair do programa\n''')

    resp = input('-> ')

    while resp not in ['0', '1', '2']:
        resp = input('\nERRO! Por favor, digite um número válido:\n-> ')
    
    return resp

def menu_dados_especificos():
    print()
    subtitulos('Gerar dado específico')
    print('''Selecione o dado que quer gerar:
    
1 - Gerar NOME

2 - Gerar CPF
          
3 - Gerar EMAIL
          
4 - Gerar ENDEREÇO
          
5 - Gerar NÚMERO DE TELEFONE\n''')

    resp = input('-> ')

    while resp not in ['1', '2', '3', '4', '5']:
        resp = input('\nERRO! Por favor, digite um número válido:\n-> ')
    
    return resp




