# -*- coding: utf-8 -*-
"""sentiment_analysis_pipeline.ipynb"""

import tensorflow_datasets as tfds
import pandas as pd
import numpy as np
import nltk
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import seaborn as sns

# Download dos recursos necessários do NLTK
nltk.download('stopwords')
nltk.download('punkt')

# 1. Carregamento e Exploração Inicial dos Dados
print("Importando o dataset de reviews IMDB...")
dataset = tfds.load('imdb_reviews', split='train', shuffle_files=True)

# Conversão dos exemplos em listas de texto e rótulos
textos = []
rótulos = []
for exemplo in dataset.take(5000):
    textos.append(exemplo['text'].numpy().decode('utf-8'))
    rótulos.append(exemplo['label'].numpy())

# Criando DataFrame para manipulação
dados = pd.DataFrame({
    'review': textos,
    'sentiment': rótulos
})

print("\nPrimeiros registros do dataset:")
print(dados.head())

print("\nInformações sobre os dados:")
print(dados.info())

print("\nDistribuição dos sentimentos:")
print(dados['sentiment'].value_counts())

# 2. Análise de Sentimentos com Hugging Face
print("\nExecutando análise de sentimentos utilizando Hugging Face...")
sentiment_pipeline = pipeline('sentiment-analysis')

def analisar_sentimento(texto):
    resultado = sentiment_pipeline(texto[:512])
    return resultado[0]

for i in range(3):
    exemplo = dados['review'].iloc[i]
    resultado = analisar_sentimento(exemplo)
    print(f"\nExemplo {i + 1}: {exemplo[:100]}...")
    print(f"Sentimento: {resultado['label']}, Score: {resultado['score']:.3f}")

# 3. Pré-processamento e Vetorização dos Dados
def limpar_texto(texto):
    """Remove stopwords e caracteres desnecessários."""
    if isinstance(texto, bytes):
        texto = texto.decode('utf-8')
    palavras = word_tokenize(str(texto).lower())
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra.isalnum() and palavra not in stopwords.words('english')]
    return ' '.join(palavras_sem_stopwords)

print("\nProcessando os textos para vetorização...")
dados['processed_review'] = dados['review'].apply(limpar_texto)

print("\nAplicando TF-IDF para transformar os textos em representações vetoriais...")
vetorizador_tfidf = TfidfVectorizer(max_features=5000)
X = vetorizador_tfidf.fit_transform(dados['processed_review'])
y = dados['sentiment']

# Dividindo os dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinamento e Avaliação de Modelos
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

# Modelos a serem avaliados
modelos = {
    'Naive Bayes': MultinomialNB(),
    'SVM': LinearSVC(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

resultados = {}
for nome, modelo in modelos.items():
    print(f"\nTreinando e avaliando modelo: {nome}")
    modelo.fit(X_treino, y_treino)
    y_predito = modelo.predict(X_teste)

    print(f"\nRelatório de classificação para {nome}:")
    print(classification_report(y_teste, y_predito))

    resultados[nome] = {
        'y_predito': y_predito,
        'relatorio': classification_report(y_teste, y_predito, output_dict=True)
    }

# 5. Visualização dos Resultados
fig, axs = plt.subplots(1, 3, figsize=(20, 5))
for idx, (nome, resultado) in enumerate(resultados.items()):
    matriz_confusao = confusion_matrix(y_teste, resultado['y_predito'])
    sns.heatmap(matriz_confusao, annot=True, fmt='d', ax=axs[idx])
    axs[idx].set_title(f'Matriz de Confusão: {nome}')
    axs[idx].set_xlabel('Previsto')
    axs[idx].set_ylabel('Real')
plt.tight_layout()
plt.show()

# Comparando as métricas de precisão, recall e F1-score entre os modelos
metricas = ['precision', 'recall', 'f1-score']
comparacao_metricas = pd.DataFrame({
    metrica: [resultados[modelo]['relatorio']['weighted avg'][metrica]
              for modelo in modelos.keys()]
    for metrica in metricas
}, index=modelos.keys())

comparacao_metricas.plot(kind='bar', figsize=(12, 6))
plt.title('Comparação de Métricas entre Modelos')
plt.ylabel('Pontuação')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()

# 6. Predição para Novos Textos
def prever_novo_texto(texto, modelo=modelos['SVM'], vetorizador=vetorizador_tfidf):
    """Realiza a previsão de sentimentos para um texto novo."""
    texto_limpo = limpar_texto(texto)
    texto_vetorizado = vetorizador.transform([texto_limpo])
    predicao = modelo.predict(texto_vetorizado)[0]
    return {
        'texto_original': texto,
        'texto_processado': texto_limpo,
        'sentimento': 'Positivo' if predicao == 1 else 'Negativo'
    }

novos_textos = [
    "The plot was amazing and the acting was excellent!",
    "I regret spending money on this boring and awful movie.",
    "It was a decent movie, with some good and bad moments."
]

print("\nClassificando novos textos:")
for texto in novos_textos:
    resultado = prever_novo_texto(texto)
    print(f"\nTexto: {resultado['texto_original']}")
    print(f"Sentimento: {resultado['sentimento']}")
