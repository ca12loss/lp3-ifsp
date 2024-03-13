# Função 
# modularizar o programa
# reuso
# manutenabilidade

# só pode acessar se a hora atual estiver entre 8h e 18h
hora_atual = 12

if hora_atual >= 8 and hora_atual <=18:
    print('permitido o acesso')

# entrada = hora_atual
# saída se está dentro ou não do horário comercial

def dentro_horario_comercial(hora_atual):
    if hora_atual >= 8 and hora_atual <=18:
        return True
    else:
        return False
    
def dentro_horario_comercial(hora_atual):
   return hora_atual >= 8 and hora_atual <=18

# Declarando uma função:
# def nome_funcao():
#   corpo da função
#   corpo da função

# Função sem retorno
# Side effect - efeito colateral
 
def diga_ola(nome):
    print(f"Olá {nome}")

# Chamada 
diga_ola('Marcio')

# Função com retorno 
def montar_frase(nome):
    return f"Olá {nome}"

nome = 'Marcio'
print(montar_frase(nome))
# envia_email(montar_frase(nome))

# Parametros e Argumentos
# Parametro são referencias podem ser acessadas dentro de função 
# Argumento são os valores passados para os parametros

def somar(numero1,numero2):
    return numero1+numero2

somar(10.0,5.0)

# Escopo de variáveis 
# Variável local 
def calcular_media(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    return media

media = calcular_media(9.9,9.1,10.0)
print(media)

# Variável global
total = 0.0

def soma(n1,n2,n3):
#   global total
    total=n1+n2+n3
    return total

print(total)
soma(1,3,5)
print(total)

# Parametros com o valor padrão (default)
def gerar_boas_vindas(nome,mensagem='Bom dia'):
    return f"{mensagem},{nome}"

print(gerar_boas_vindas('Marcio','Bom Dia'))
print(gerar_boas_vindas('Marcio','Bom Noite'))
print(gerar_boas_vindas('Maria'))

# Argumentos nomeados

print(gerar_boas_vindas(nome='Maria'))

# docstring (comentários de documentação)
# documentar classe, módulos, funções,...

def somar(numero1,numero2):
    '''
    Função que realiza a soma de dois números
    :param numero1: primeiro número
    :param numero2: segundo número
    :return: a soma dos números
    '''
    return numero1+numero2

#Funções built in
# print, type, len, sum, max