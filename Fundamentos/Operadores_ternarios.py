# Operadores Ternários

esta_chuvendo = True

# Primeira condição é falsa  e a segunda é falsa
print('Hoje estou com as roupas' + (' secas. ', ' molhadas ')[esta_chuvendo]
      )

idade = 21

print('Você ' + ('não pode entrar na festa','pode entrar na festa')[idade > 18])

altura = 6.1

print('Você ' + ('não pode subir no brinquedo'if altura <  5 else 'pode subir no brinquedo'))
