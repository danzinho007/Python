import random

# O banco de dados é uma lista de tuplas, onde cada tupla contém uma pergunta e uma lista de 4 respostas
database = [
    ("Qual é a capital do Japão?", ["Tóquio", "Nagoya", "Ōsaka", "Kyōto"]),
    ("Qual é a maior cidade do Japão?", ["Yokohama", "Nagoya", "Tóquio", "Ōsaka"]),
    ("Qual é a segunda maior cidade do Japão?", ["Ōsaka", "Tóquio", "Nagoya", "Kyōto"]),
    ("Qual é a terceira maior cidade do Japão?", ["Nagoya", "Tóquio", "Ōsaka", "Kyōto"])
]

# Crie uma lista para armazenar as perguntas já usadas
used_questions = []

# Inicialize a pontuação do usuário em 0
pontos = 0

# Inicie o contador de perguntas com 0
perguntas = 0

while True:
    # Verifique se todas as perguntas foram usadas
    if len(used_questions) == len(database):
        # Limpe a lista de perguntas usadas
        used_questions = []
        # Limpe a lista de perguntas corretas
        correct_questions = []
        # Redefina a variável de pontos
        pontos = 0
        print("Todas as perguntas foram usadas. O jogo será reiniciado.")

    # Escolha uma pergunta aleatória do banco de dados que ainda não foi usada
    question_index = random.randint(0, len(database)-1)
    while question_index in used_questions or question_index in correct_questions:
        question_index = random.randint(0, len(database)-1)
    used_questions.append(question_index)

    # Obtenha a pergunta e as respostas da tupla selecionada
    question, answers = database[question_index]

    # Misture aleatoriamente a ordem das respostas
    random.shuffle(answers)

    # Imprima a pergunta e as respostas
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}: {answer}")

    # Peça ao usuário para escolher uma resposta
selected_answer = int(input("Qual é a sua resposta? "))

# Verifique se a resposta escolhida é correta
if answers[selected_answer-1] == "Tóquio":
    print("Parabéns, sua resposta está correta")
    pontos += 1
    # Adicione a pergunta correta à lista de perguntas usadas
    correct_questions.append(question_index)
else:
    print("Desculpe, sua resposta está incorreta")

# Verifique se o jogador deseja continuar jogando
continuar = input("Deseja continuar jogando? (s/n) ")
if continuar.lower() == "n":
    break

# Imprima uma mensagem de despedida
print("Obrigado por jogar!")

