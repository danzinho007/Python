# A até Z 
# Resultado final esperado :
# A
# A B 
# A B C
# até Z

from string import ascii_uppercase

def print_pattern():
    for i in range(1, len(ascii_uppercase) +1):
        print(" ". join(ascii_uppercase[j] for j in range (i)))
print_pattern()
