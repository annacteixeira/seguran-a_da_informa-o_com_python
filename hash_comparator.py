import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
with open(file1, 'rb') as f1:
    hash1.update(f1.read())

hash2 = hashlib.new('ripemd160')
with open(file2, 'rb') as f2:
    hash2.update(f2.read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {file1} é diferente do arquivo: {file2}.')
    print(f'O hash do arquivo: {file1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo: {file2} é: {hash2.hexdigest()}')

else:
    print(f'O arquivo: {file1} é igual ao arquivo: {file2}.')
    print(f'O hash do arquivo: {file1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo: {file2} é: {hash2.hexdigest()}')