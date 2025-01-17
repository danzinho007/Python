import requests
import json
import joblib  # Esta biblioteca é usada para salvar e carregar modelos treinados
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

# Obter dados da API
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['data']
else:
    print(f"Erro na solicitação: {response.status_code}")

# Preparar dados para o modelo
X = [card['desc'] for card in data]
y = [card['type'] for card in data]

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo usando um pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Acurácia do modelo:", accuracy)

# Salvar o modelo treinado em um arquivo
joblib.dump(model, 'modelo_yugioh.joblib')

# Carregar o modelo treinado
modelo_carregado = joblib.load('modelo_yugioh.joblib')

# Fazer previsões com o modelo carregado
novos_dados = ["Descrição da nova carta"]
previsoes = modelo_carregado.predict(novos_dados)
print("Previsões:", previsoes)
