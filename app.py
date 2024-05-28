import random

# Listas geradas aleatoriamente
nomes = ['Anna Liz Alves', 'Sofia Costela', 'Laura Aparecida', 'Marcela Mendonça', 'Fernanda Gomes']
emails = ['eduardasa@example.com', 'vianadom@example.org', 'ravibarros@example.com', 'mouramaria-sophia@example.com', 'vicentevasconcelos@example.com']
telefones = ['(081) 8232 1593', '+55 81 5790 1881', '0300 978 8781', '0500-939-7055', '21 3483-6385']
cidades = ['Pinto de Siqueira', 'Cassiano', 'Mendes', 'Vargas de Marques', 'Sampaio do Oeste']
estados = ['Mato Grosso', 'Acre', 'Paraíba', 'Amazonas', 'Pará']

# Menu de escolha do usuário
print('Escolha uma das opções abaixo a serem geradas aleatoriamente: \n')
print('[1] - Nome')
print('[2] - Email')
print('[3] - Telefone')
print('[4] - Cidade')
print('[5] - Estado')
print('[0] - Sair')

# # Fazendo com que o usuário digite sempre entre um numero de 1 a 5
while True:
    try:
        opcoes = input('\nDigite o número da(s) opção(ões) desejada(s), separadas por vírgula (ou 0 para sair): ').split(',')
        opcoes_numericas = [int(i) for i in opcoes]
        print()

        for opcao in opcoes_numericas:
            if opcao == 0:
                print('Saindo... ')
                exit()

            elif 1 <= opcao <= 5:
                if opcao == 1:
                    print(random.choice(nomes))
                if opcao == 2:
                    print(random.choice(emails))
                if opcao == 3:
                    print(random.choice(telefones))
                if opcao == 4:
                    print(random.choice(cidades))
                if opcao == 5:
                    print(random.choice(estados))
                
            else:
                print(f'A opção {opcao} não é válida')
        
        print()
        escolha = input('Deseja continuar? (Digite "s" para sim, ou pressione qualquer tecla para sair): \n')

        if escolha.lower() != 's':
            print('Saindo... ')
            break

    except ValueError:
        print('Digite um valor numérico entre 0 e 5 \n')



