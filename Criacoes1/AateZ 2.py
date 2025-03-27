# A até Z 
# Resultado final esperado :
# A
# A B 
# A B C
# até Z

import os
from string import ascii_uppercase

def print_pattern_to_file():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder_path, "AateZ.txt")
    with open(file_path, "w") as file:
        for i in range(1, len(ascii_uppercase) + 1):
            line = " ".join(ascii_uppercase[j] for j in range(i)) + "\n"
            file.write(line)

print_pattern_to_file()
