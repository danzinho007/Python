from decimal import Decimal, getcontext

# Defina a precisão desejada
getcontext().prec = 100  # Ajuste a precisão conforme necessário

# Defina o nível inicial e a experiência inicial como objetos Decimal
nivel = Decimal("1")
experiencia = Decimal("5")

# Defina até que nível você deseja calcular a experiência
nivel_maximo = 1000000

# Loop para calcular a experiência para cada nível
for i in range(int(nivel), int(nivel_maximo) + 1):
    print(f"Lv {nivel} = {experiencia} exp")
    nivel += Decimal("1")
    experiencia *= Decimal("2")
