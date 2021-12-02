import hashlib


def main():
    frase = input('Digite o texto a ser transformado em hash: ').strip()
    while True:
        algoritmo = int(input('Digite a opção desejada para o algoritmo\n'
                              '1- MD5\n'
                              '2- SHA1\n'
                              '3- SHA256\n'
                              '4- SHA512\n'
                              'Escolha: '))
        if 1 <= algoritmo <= 4:
            break
    resultado = hashlib.md5(frase.encode('utf-8')) if algoritmo == 1 else \
        hashlib.sha1(frase.encode('utf-8')) if algoritmo == 2 else \
        hashlib.sha256(frase.encode('utf-8')) if algoritmo == 3 else \
        hashlib.sha512(frase.encode('utf-8'))
    print(f'O hash da string "{frase}" é: {resultado.hexdigest()}')


if __name__ == '__main__':
    main()
