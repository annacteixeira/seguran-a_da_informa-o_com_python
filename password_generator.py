import random, string

size = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'çÇ!@#$%&*()-=+/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))
