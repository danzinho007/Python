print("\nWrite a program that reads a value in meters and displays it converted into centimeters and millimeters.")

# Lembrando : 
# Quilômetro, Hectômetro, Decâmetro, Metro
# Decímetro, Centímetro, Milímetro
# Km Hm Dam M Dm Cm Mm
#  1  0  0 0  0  0  0 = 1km = 1 000m = 100 000mm
# Ou seja : 1km > m é 1 x 1000 = 1000m
# 1m = 0,001 km
# Ou seja : 1m > km é 1 / 1000 = 0,001km

metro=float(input("\nDigite o valor em metros que deseja converter : "))

print(f"{metro} em cm fica : {metro*0.001:.3f} km")
print(f"{metro} em cm fica : {metro*0.01:.2f} hm")
print(f"{metro} em cm fica : {metro*0.1:.1f} dam")
print(f"{metro} em cm fica : {metro*10} dm")
print(f"{metro} em cm fica : {metro*100} cm")
print(f"{metro} em cm fica : {metro*100} mm\n")
