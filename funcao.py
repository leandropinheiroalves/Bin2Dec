def binario():
    while True:
        try:
            numero = int(input('Digite um número binário de até 8 digitos: '), 2)
            string_numero = bin(numero)
            while len(string_numero[2:]) > 8:
                print('ERRO! O número digitado precisa ter no máximo 8 digitos!')
                numero = int(input('Digite um número binário de até 8 digitos: '), 2)
                string_numero = bin(numero)
        except ValueError:
            print('ERRO! Só podem ser inseridos os digitos 0 ou 1!')
        else:
            print(f'O número decimal referente ao número binário "{string_numero[2:]}" é {numero}')
            break


if __name__ == '__main__':
    binario()
