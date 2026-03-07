import secrets
import string

alfabeto = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(secrets.choice(alfabeto) for i in range(12))
print(senha)

# token = secrets.token_hex(16)
# print(token)

# if secrets.compare_digest(senha_usuario, senha_armazenada):
#     print("Acesso permitido")



import random
 
def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
 
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),     
        random.choice(especiais)    
    ]
 
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)
 
print(f"Senha gerada: {gerar_senha()}")
