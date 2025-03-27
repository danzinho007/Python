import random

def gerar_senha():
    """Gera uma senha aleatória de 5 dígitos"""
    return [random.randint(0, 9) for _ in range(5)]

def verificar_tentativa(senha, tentativa):
    """Compara a tentativa do usuário com a senha"""
    corretos = 0
    for i in range(5):
        if senha[i] == tentativa[i]:
            corretos += 1
    return corretos

def main():
    print("=== Jogo de Adivinhar a Senha ===")
    print("A senha tem 5 dígitos (0 a 9). Tente adivinhar!")
    print("Dica: O programa mostrará quantos dígitos estão corretos e em suas posições.\n")
    
    senha = gerar_senha()
    tentativas = 0
    
    while True:
        try:
            # Pede ao usuário para digitar uma tentativa
            tentativa = input("Digite sua tentativa (5 dígitos): ")
            if len(tentativa) != 5 or not tentativa.isdigit():
                print("Entrada inválida! Digite exatamente 5 dígitos.")
                continue
            
            tentativa_lista = [int(digito) for digito in tentativa]
            tentativas += 1
            
            # Verifica a quantidade de dígitos corretos
            corretos = verificar_tentativa(senha, tentativa_lista)
            
            if corretos == 5:
                print(f"\nParabéns! Você adivinhou a senha em {tentativas} tentativas.")
                break
            else:
                print(f"Você acertou {corretos} dígitos na posição correta. Tente novamente!\n")
        
        except KeyboardInterrupt:
            print("\nJogo encerrado pelo usuário. Até mais!")
            break

if __name__ == "__main__":
    main()
