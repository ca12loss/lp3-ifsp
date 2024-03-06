# operadores aritiméticos
# +, -, *, /, %, **

nota1 = 3.0
nota2 = 5.5
media = (nota1+nota2)/2

# 2 elevado ao quadrado
potencia = 2 ** 2

# 2 elevado ao cubo
#potencia = 2*** 2
numero = 2*2*2

# operadores de atribuição 
# =, +=, -= ...
#idade += 10

#operadores lógicos 
# and, or, not

resultado = True and False
print(type(resultado))
print(resultado)

# and 
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0


#operadores de comparação
# ==, !=, >,<, >=, <=

idade = 17
maior_de_idade = idade >= 18

if maior_de_idade:
    print('Maior de idade')
else:
    print('Menor')

#operador is
# os valores do objeto e se ocupam o mesmo
#espaço de memoória

a = [1,2,3]
b = [1,2,3]

print(a is b)
print(a==b)

z = [1,2,3]
x = z
print(z is x)

# operador in e not in
# verificar se um objeto está ou não
# dentro de uma sequencia (str, list, tuple ...)

print('a' in 'Java')
print('Maria' in ['Pedro', 'Ana'])

alunos = ['Pedro','Ana']
aluno = 'Maria'
print(aluno in alunos)
print(aluno not in alunos)

