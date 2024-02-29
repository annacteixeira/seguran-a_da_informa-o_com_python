import os #Importa o módulo ou biblioteca os (integra os programas e recursos do sistema operacional)

print('#' * 60) #Imprime # 60 vezes

#Variável que recebe do usuário um IP ou Host
ip_or_host = input("Digite o IP ou Host a ser verificado: ")
print('-' * 60) #Imprime - 60 vezes

os.system('ping -n 6 {}'.format(ip_or_host)) #Chama o método system do módulo os - comando ping
# -n = número de pacotes

print('-' * 60) #Imprime - 60 vezes