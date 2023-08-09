import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pytesseract
import cv2

# Dados de treinamento para o modelo de análise de sentimento
data = [
    ("Eu amo este produto! É incrível.", "positivo"),
    ("Muito bom", "positivo"),
    ("Muito ruim", "negativo"),
    ("Gostei", "positivo"),
    ("Não gostei", "negativo"),
    ("Minha experiência com o produto foi muito boa.", "positivo"),
    ("Este produto é de baixa qualidade.", "negativo"),
    ("Estou muito desapontado com a compra.", "negativo"),
    ("Excelente serviço ao cliente!", "positivo"),
    ("Péssimo atendimento ao cliente.", "negativo"),
    ("Ótimo custo-benefício.", "positivo"),
    ("Não vale o preço cobrado.", "negativo"),
    ("Recomendo a todos!", "positivo"),
    ("Não recomendo a ninguém.", "negativo"),
    ("Superou minhas expectativas.", "positivo"),
    ("Uma grande decepção.", "negativo"),
    ("Entrega rápida e eficiente.", "positivo"),
    ("Demorou muito para entregar.", "negativo"),
    ("Funciona perfeitamente.", "positivo"),
    ("Não funciona como prometido.", "negativo"),
    ("Satisfeito com a compra.", "positivo"),
    ("Arrependido da compra.", "negativo"),
    ("Produto de alta qualidade.", "positivo"),
    ("Produto de baixa qualidade.", "negativo"),
    ("Estou feliz com minha compra.", "positivo"),
    ("Me sinto enganado.", "negativo"),
    ("Fácil de usar e configurar.", "positivo"),
    ("Difícil de usar e configurar.", "negativo"),
    ("Muito feliz com minha escolha.", "positivo"),
    ("Muito insatisfeito.", "negativo"),
    ("Muito satisfeito.", "negativo"),
]

vetorizador = TfidfVectorizer()
X = vetorizador.fit_transform([texto for texto, _ in data])
y = [rotulo for _, rotulo in data]

# Treinamento do modelo de análise de sentimento
modelo = MultinomialNB()
modelo.fit(X, y)

def realizar_analise_sentimento(texto):
    # Vetoriza o texto de entrada
    vetor_entrada = vetorizador.transform([texto])
    # Faz a previsão do sentimento utilizando o modelo treinado
    rotulo_previsto = modelo.predict(vetor_entrada)[0]
    return rotulo_previsto

def analisar_texto(texto):
    return realizar_analise_sentimento(texto)

def analisar_imagem(bytes_imagem):
    img = cv2.imdecode(np.frombuffer(bytes_imagem, np.uint8), cv2.IMREAD_COLOR)
    texto = pytesseract.image_to_string(img)
    return realizar_analise_sentimento(texto)
