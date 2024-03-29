# Executar com F5

#010 : Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considera U$$1.00 = R$ 3.27

print('Saiba aqui quantos dólares você tem ? R$')
print('Pode por os centavos também')
nDin = float(input('Digite aqui quantos reais possui : '))
dolar = ( nDin * 1.00 ) / 3.27
# ou
dolar1 = nDin / 3.27

input('Tendo em consideração 1 dólar = 3.27, você tem {:.2f} U$$' .format(dolar))
input('Tendo em consideração 1 dólar = 3.27, você tem {:.2f} U$$' .format(dolar1))
print(' ')