# Executar com F5

#007 : Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra sua média

print(' ')
print('Saiba aqui a sua média')
n2 = int(input('Digite aqui quanto você tirou no Teste : '))
n3 = int(input('Digite aqui quanto você tirou na Prova : '))
media = ( n2 + n3 ) / 2
input('A média do aluno que tirou {:.1f} com {:.1f} é {:.1f}' .format(n2, n3, media))
#ou
input('A média do aluno que tirou {:.1f} com {:.1f} é {:.1f}' .format(n2, n3, ((n2 + n3) / 2)))

