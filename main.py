import hashlib

'''
euuu sabo
sabo sapu
muto snha
'''

ARQUIVO = 'usuarios.txt'

# Função para salvar usuário e senha no arquivo
def salvar_arquivo(nome_arquivo, nome_usuario, senha):
    with open(nome_arquivo, 'a+') as arquivo:
        hash_senha = hashlib.sha256(senha.encode())
        hash_senha = hash_senha.hexdigest()
        arquivo.write(f"{nome_usuario},{hash_senha}\n")

# Função para ler usuários e senhas do arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        usuarios = []
        for linha in linhas:
            usuario, senha = linha.strip().split(",")
            usuarios.append((usuario, senha))

    return usuarios

# Função para criar um novo usuário
def criar_usuario(nome_arquivo):
    nome_usuario = input("Digite seu usuário: ")
    senha_usuario = input("Digite sua senha: ")
    salvar_arquivo(nome_arquivo, nome_usuario, senha_usuario)

# Função para autenticar o usuário
def autenticar_usuario(nome_usuario, senha_usuario, usuarios):
    for usuario in usuarios:
        nome = usuario[0]
        senha = usuario[1]
        senha_hash = hashlib.sha256(senha_usuario.encode()).hexdigest()

        if nome == nome_usuario and senha == senha_hash:
            return True

    return False


resposta = int(input('Digite 1 para se cadastrar e 2 para logar: '))


if resposta == 1:
    criar_usuario(ARQUIVO)


elif resposta == 2:
    i = 0
    while True:
        
        usuarios = ler_arquivo(ARQUIVO)
        nome_usuario = input("Digite seu usuário: ")
        senha_usuario = input("Digite sua senha: ")
        if i < 2:
            if autenticar_usuario(nome_usuario, senha_usuario, usuarios):
                print('Autenticado com sucesso!')
                break
            else:
                i += 1
                print('Usuário ou senha incorretos. Tente novamente.')
        else:
            print('Você atingiu o numero maximo de tentativas')
            break
            
else:
    print('Resposta inválida.')
    
