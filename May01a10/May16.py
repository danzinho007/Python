print("\n# Write a program that converts a temperature entered in degrees Celsius to degrees Fahrenheit.")

# Lembrando :
# Celsius > Kelvin : Tk = Tc + 273
# Celsius > Fahrenheit : Tf = 1.8 * Tc + 32
# Kelvin > Celsius : Tc = Tk - 273
# Kelvin > Fahrenheit : Tf = 1.8 * ( Tk - 273 )
# Fahrenheit > Celsius : Tc = ( Tf - 32 ) * 5 / 9
# Farhrenheit > Kelvin : Tk = ( Tf - 32 ) * 5 / 9 + 273

celsius=float(input("\nInforme a temperatura em °Celsius : "))
print(f"°{celsius} em Kelvin é {celsius + 273}")
print(f"°{celsius} em Fahrenheit é de {1.8 * celsius + 32}")

kelvin=float(input("\nInforme a temperatura em Kelvin : "))
print(f"{kelvin} em Celsius é {kelvin - 273}")
print(f"{kelvin} em Fahrenheit é de {1.8 * ( kelvin - 273)}")

fahrenheit=float(input("\nInforme a temperatura em °Fahrenheit : "))
print(f"°{fahrenheit} em Celsius é {( fahrenheit - 32 ) * 5 / 9 }")
print(f"°{fahrenheit} em Kelvin é de { (fahrenheit - 32 ) * 5 / 9 + 273}")
