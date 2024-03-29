# Executar com F5

A = {1, 2, 3}
B = {3, 4, 5, 6}
C = {5, 6}

# União
print( A | B ) # Retorna {1,2,3,4,5,6}
print( A | C ) # Retorna {1,2,3,5,6}
print( B | C ) # Retorna {3,4,5,6}
print( A | B | C) # Retorna {1,2,3,4,5,6}

# Interseção
print( A & B )
print( A & C )
print( B & A )
print( B & C )
print( C & A )
print( C & B )
print( A & B & C )

# Diferença 
print( A - B )
print( A - C )
print( B - A )
print( B - C )
print( C - A )
print( C - B )
print( A - B - C )

# Diferença Simétrica
print( A ^ B )
print( A ^ C )
print( B ^ A )
print( B ^ C )
print( C ^ A )
print( C ^ B )
print( A ^ B ^ C )

# Pertinência
print( 1 in A )
print( 4 in A )
print( 1 in B )
print( 3 in B )
print( 4 in C )
print( 5 in C )
print( 1 in A and 2 in A )
print( 1 in A and 4 in A )
# Ao invés de usar and, pode usar or ou not

# Não-Pertinência
print( 1 not in A )
print( 4 not in A )
print( 1 not in B )
print( 3 not in B )
print( 4 not in C )
print( 5 not in C )
print( 1 not in A and 2 not in A )
print( 1 not in A and 4 not in A )

# Subconjunto
print( A <= B)
print( A <= C)
print( B <= A)
print( B <= C)
print( C <= A)
print( C <= B)
print( A <= B and A <= C)

# Superset
print( A >= B)
print( A >= C)
print( B >= A)
print( B >= C)
print( C >= A)
print( C >= B)
print( A >= B and A >= C)

# Subconjunto Próprio
print( A < B)
print( A < C)
print( B < A)
print( B < C)
print( C < A)
print( C < B)
print( A < B and A < C)

# Superset Próprio
print( A > B)
print( A > C)
print( B > A)
print( B > C)
print( C > A)
print( C > B)
print( A > B and A > C)
