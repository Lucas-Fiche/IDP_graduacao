import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
import warnings
warnings.filterwarnings('ignore')

def carregar_e_explorar_dados():
    """Importa e realiza uma análise inicial do dataset"""
    print("1. Explorando o Conjunto de Dados")

    # Leitura do arquivo CSV
    url = 'https://raw.githubusercontent.com/klaytoncastro/idp-machinelearning/refs/heads/main/clustering/mall_customers.csv'
    dados = pd.read_csv(url)
    print("\nPrimeiras entradas do dataset:")
    print(dados.head())

    # Transformação da variável categórica
    encoder = LabelEncoder()
    dados['Gender'] = encoder.fit_transform(dados['Gender'])

    # Visualização das distribuições e detecção de outliers
    colunas_numericas = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    for idx, coluna in enumerate(colunas_numericas):
        # Histogramas
        sns.histplot(data=dados, x=coluna, kde=True, ax=axes[0, idx])
        axes[0, idx].set_title(f'Distribuição: {coluna}')

        # Boxplots
        sns.boxplot(data=dados, y=coluna, ax=axes[1, idx])
        axes[1, idx].set_title(f'Detecção de Outliers: {coluna}')
    plt.tight_layout()
    plt.show()

    # Relações entre variáveis
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=dados, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', style='Gender')
    plt.title('Renda Anual vs Score de Gastos')

    plt.subplot(1, 2, 2)
    sns.scatterplot(data=dados, x='Age', y='Spending Score (1-100)', hue='Gender', style='Gender')
    plt.title('Idade vs Score de Gastos')
    plt.tight_layout()
    plt.show()

    # Correlações entre variáveis
    plt.figure(figsize=(10, 8))
    matriz_correlacao = dados[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].corr()
    sns.heatmap(matriz_correlacao, annot=True, cmap='viridis', center=0)
    plt.title('Mapa de Correlação')
    plt.show()

    return dados

def preparar_dados(dados):
    """Transforma as features em formato escalado para clusterização"""
    print("\n2. Preparação dos Dados para Clustering")

    # Criação de diferentes subconjuntos de features
    conjuntos_features = {
        'renda_score': ['Annual Income (k$)', 'Spending Score (1-100)'],
        'completo': ['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    }

    dados_escalados = {}
    escalador = StandardScaler()

    for nome, features in conjuntos_features.items():
        matriz = dados[features].values
        matriz_escalada = escalador.fit_transform(matriz)
        dados_escalados[nome] = matriz_escalada

    return dados_escalados, conjuntos_features

def clustering_hierarquico(X, nomes_features):
    """Executa a clusterização hierárquica e exibe os resultados"""
    print("\n3. Clusterização Hierárquica")

    # Construção do linkage para o dendrograma
    matriz_ligacao = linkage(X, method='ward')

    # Exibição do dendrograma
    plt.figure(figsize=(10, 7))
    dendrogram(matriz_ligacao)
    plt.title('Dendrograma - Clustering Hierárquico')
    plt.xlabel('Amostras')
    plt.ylabel('Distância')
    plt.show()

    # Aplicação do modelo hierárquico
    modelo_hc = AgglomerativeClustering(n_clusters=5)
    rotulos = modelo_hc.fit_predict(X)

    # Visualização dos grupos formados
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=rotulos, cmap='tab10')
    plt.xlabel(nomes_features[0])
    plt.ylabel(nomes_features[1])
    plt.title('Clusterização Hierárquica - Grupos')
    plt.colorbar(scatter)
    plt.show()

    return rotulos

def otimizar_kmeans(X):
    """Determina o número ideal de clusters usando métodos visuais"""
    print("\n4. Determinando o Número Ideal de Clusters")

    max_clusters = 10
    inercia = []
    silhouette_scores = []

    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inercia.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X, kmeans.labels_))

    # Exibição dos resultados
    plt.figure(figsize=(12, 5))

    # Método do Cotovelo
    plt.subplot(1, 2, 1)
    plt.plot(range(2, max_clusters + 1), inercia, 'bo-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Inércia')
    plt.title('Método do Cotovelo')

    # Análise Silhouette
    plt.subplot(1, 2, 2)
    plt.plot(range(2, max_clusters + 1), silhouette_scores, 'ro-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Índice Silhouette')
    plt.title('Análise de Silhouette')

    plt.tight_layout()
    plt.show()

    k_otimo = np.argmax(silhouette_scores) + 2
    return k_otimo

def aplicar_algoritmos_clustering(X, nomes_features, num_clusters):
    """Realiza a clusterização usando K-means e DBSCAN"""
    print("\n5. Aplicação de Algoritmos de Clusterização")

    # Algoritmo K-means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    rotulos_kmeans = kmeans.fit_predict(X)

    # Algoritmo DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    rotulos_dbscan = dbscan.fit_predict(X)

    # Exibição dos resultados
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Gráficos K-means
    scatter1 = axes[0].scatter(X[:, 0], X[:, 1], c=rotulos_kmeans, cmap='tab10')
    axes[0].set_xlabel(nomes_features[0])
    axes[0].set_ylabel(nomes_features[1])
    axes[0].set_title('Grupos - K-means')
    plt.colorbar(scatter1, ax=axes[0])

    # Gráficos DBSCAN
    scatter2 = axes[1].scatter(X[:, 0], X[:, 1], c=rotulos_dbscan, cmap='tab10')
    axes[1].set_xlabel(nomes_features[0])
    axes[1].set_ylabel(nomes_features[1])
    axes[1].set_title('Grupos - DBSCAN')
    plt.colorbar(scatter2, ax=axes[1])

    plt.tight_layout()
    plt.show()

    return rotulos_kmeans, rotulos_dbscan, kmeans.cluster_centers_

def main():
    # 1. Carregamento e exploração
    dados = carregar_e_explorar_dados()

    # 2. Preparação dos dados
    dados_escalados, conjuntos_features = preparar_dados(dados)

    # 3. Análise para cada conjunto de variáveis
    for nome, X in dados_escalados.items():
        print(f"\nResultados para o conjunto: {nome}")
        nomes_features = conjuntos_features[nome]

        # Clusterização Hierárquica
        rotulos_hierarquicos = clustering_hierarquico(X, nomes_features)

        # Número ótimo de clusters
        k_otimo = otimizar_kmeans(X)
        print(f"Número ótimo de clusters: {k_otimo}")

        # Aplicação de clustering
        rotulos_kmeans, rotulos_dbscan, _ = aplicar_algoritmos_clustering(X, nomes_features, k_otimo)

if __name__ == "__main__":
    main()
