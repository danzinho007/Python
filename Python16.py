# Executar com F5

#008 : Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm

print(' ')
# km hm dam m dm cm mm
# 1  0   0  0  0  0  0 = 1 km tem 10 hm, 100 dam ou 1.000 m
# 0  0   0  1  0  0  0 = 1  m tem 10 dm, 100  cm ou 1.000 mm
# 0, 0   0  0  0  0  1 = 1 mm tem 0,000.001 km
# 0  0   0  0, 0  0  1 = 1 mm tem 0,001 m

print('Saiba aqui quantos dm, cm e mm tem qualquer metro')
n4 = int(input('Digite aqui o valor : '))
dm = n4 * 10
cm = n4 * 100
mm = n4 * 1000
input('A medida de {} é de {:.0f} dm, {:.0f} cm e {:.0f}mm' .format(n4, dm, cm, mm))

