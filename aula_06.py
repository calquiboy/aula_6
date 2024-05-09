
# desafio
    
# sistema de senhas
# o computador cria uma senha aleatória
# vc precisa digitar a senha de acesso
# verificar se o usuario pode acessar o sistema
import random

senha_aleatoria = random.randint(10,20)

chute_senha = int(input('Digite sua senha: '))

if chute_senha == senha_aleatoria:
    print('Senha Correta, Seja bem-vindo!', senha_aleatoria)
else:
    print('Senha Incorreta, tente novamente!', senha_aleatoria)