import os

# Função para ler os IPs de um arquivo
def ler_ips(arquivo):
    with open(arquivo, 'r') as file:
        ips = file.readlines()
    return [ip.strip() for ip in ips]

# Função para fazer o ping
def ping(ip):
    resposta = os.system("ping -c 1 " + ip)
    return resposta == 0

# Ler os IPs do arquivo
ips = ler_ips('ips.txt')

# Listas para armazenar os resultados
respondidos = []
nao_respondidos = []

# Testar cada IP
for ip in ips:
    if ping(ip):
        respondidos.append(ip)
    else:
        nao_respondidos.append(ip)

# Salvar os resultados em arquivos
with open('respondidos.txt', 'w') as file:
    for ip in respondidos:
        file.write(ip + '\n')

with open('nao_respondidos.txt', 'w') as file:
    for ip in nao_respondidos:
        file.write(ip + '\n')

# Exibir os resultados
print("Respondidos:", respondidos)
print("Não Respondidos:", nao_respondidos)
