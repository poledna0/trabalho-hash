import hashlib

'''
euuu sabo
sabo sapu
muto snha
'''

ARQUIVO = 'usuarios.txt'


def salvar_arquivo(nome_arquivo, nome_usuario, senha):
    with open(nome_arquivo, 'a+') as arquivo:
        hash_senha = hashlib.sha256(senha.encode())
        hash_senha = hash_senha.hexdigest()
        arquivo.write(f"{nome_usuario},{hash_senha}\n")


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        usuarios = []
        for linha in linhas:
            usuario, senha = linha.strip().split(",")
            usuarios.append((usuario, senha))

    return usuarios


def criar_usuario(nome_arquivo, usuario, senha):
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    salvar_arquivo(nome_arquivo, usuario, senha)


# Criando usuário
# criar_usuario('usuarios.txt', 'euuu', 'sabo')
# criar_usuario('usuarios.txt', 'sabo', 'sapu')
# criar_usuario('usuarios.txt', 'muto', 'snha')

# Identificação do usuário
usuarios = ler_arquivo(ARQUIVO)

nome_usuario = input("Digite seu usuário: ")
senha_usuario = input("Digite sua senha: ")

# hash_senha = hashlib.sha256(senha.encode())
# hash_senha = hash_senha.hexdigest()

usuario_existe = False
for usuario in usuarios:
    nome = usuario[0]
    senha = usuario[1]
    if nome == nome_usuario:
        print('user existe')
        usuario_existe = True

if usuario_existe == False:
    salvar_arquivo(ARQUIVO, nome_usuario, senha_usuario)

# SUBSTITUIR POR CÓDIGO
# Verifico nome de usuário e, se existir, mostro que o usuário existe e paro execução do loop (break)
# Senão, mostro que o usuário não existe e paro execução do loop (break)
# FIM SUBSTITUIR POR CÓDIGO

for usuario in usuarios:
    nome = usuario[0]
    senha = usuario[1]
    senha_hash = hashlib.sha256(senha_usuario.encode())
    senha_hash = senha_hash.hexdigest()

    if senha_hash == senha:
        print('autenticado')


# SUBSTITUIR POR CÓDIGO
# Verifico nome de usuário e, se existir, faço autenticação comparando senha fornecida pelo teclado
# com senha armazenada na variável 'senha'.
#   Se as senhas forem iguais, então mostre para o usuário "Seja bem vindo" e pare a execução do loop (break)
#   Senão, mostre "Usuário ou senha incorreto" e pare a execução do loop (break)
# FIM SUBSTITUIR POR CÓDIGO
