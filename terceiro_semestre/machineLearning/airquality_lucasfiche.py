import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def carregar_dados():
    """Leitura e ajustes iniciais no conjunto de dados"""
    print("1. Importando dataset...")
    url = 'https://raw.githubusercontent.com/klaytoncastro/idp-storytelling/master/airquality/airquality.csv'
    dados = pd.read_csv(url, delimiter=';', decimal=',')

    # Conversão para formato datetime e limpeza de colunas
    dados['DataHora'] = pd.to_datetime(dados['Date'] + ' ' + dados['Time'], format='%d/%m/%Y %H.%M.%S')
    dados.drop(columns=['Date', 'Time'], inplace=True)

    # Substituição de valores nulos e exclusão de colunas desnecessárias
    dados.replace(-200, np.nan, inplace=True)
    dados.drop(columns=['NMHC(GT)'], inplace=True)

    # Preenchimento dos valores ausentes
    dados = dados.fillna(method='ffill').fillna(method='bfill')

    return dados

def explorar_dados(dados):
    """Exploração inicial dos dados para entender padrões e distribuições"""
    print("\n2. Explorando dataset...")

    # Visualização de outliers para algumas variáveis
    poluentes = ['CO(GT)', 'NO2(GT)', 'NOx(GT)', 'C6H6(GT)']
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    for idx, pol in enumerate(poluentes):
        ax = axs[idx//2, idx%2]
        sns.boxplot(data=dados, y=pol, ax=ax)
        ax.set_title(f'Boxplot de {pol}')
    plt.tight_layout()
    plt.show()

    # Correlação entre variáveis
    plt.figure(figsize=(12, 8))
    sns.heatmap(dados.corr(), annot=True, cmap='viridis', fmt='.2f')
    plt.title('Correlação entre Variáveis')
    plt.show()

    # Análise temporal das medições
    dados.set_index('DataHora', inplace=True)
    fig, axs = plt.subplots(2, 1, figsize=(15, 10))

    media_diaria = dados['CO(GT)'].resample('D').mean()
    axs[0].plot(media_diaria.index, media_diaria.values)
    axs[0].set_title('Variação Diária de CO')

    media_horaria = dados.groupby(dados.index.hour)['CO(GT)'].mean()
    axs[1].plot(media_horaria.index, media_horaria.values)
    axs[1].set_title('Padrão Horário de CO')
    plt.tight_layout()
    plt.show()

    return dados

def preparar_variaveis(dados):
    """Geração de novas variáveis e separação em atributos e alvo"""
    print("\n3. Criando variáveis derivadas...")

    # Extração de informações temporais
    dados['Hora'] = dados.index.hour
    dados['Mes'] = dados.index.month
    dados['DiaSemana'] = dados.index.dayofweek

    # Transformação cíclica de variáveis sazonais
    dados['SenoHora'] = np.sin(2 * np.pi * dados['Hora']/24)
    dados['CossenoHora'] = np.cos(2 * np.pi * dados['Hora']/24)
    dados['SenoMes'] = np.sin(2 * np.pi * dados['Mes']/12)
    dados['CossenoMes'] = np.cos(2 * np.pi * dados['Mes']/12)

    # Seleção de colunas para análise
    atributos = ['PT08.S1(CO)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)',
                 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)',
                 'T', 'RH', 'AH', 'SenoHora', 'CossenoHora', 'SenoMes', 'CossenoMes',
                 'DiaSemana']

    X = dados[atributos]
    y = dados['CO(GT)']

    return X, y, atributos

def treinar_modelos(X, y):
    """Treinamento dos modelos e avaliação com validação cruzada"""
    print("\n4. Avaliando modelos...")

    # Separação dos dados e padronização
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
    escalador = StandardScaler()
    X_treino_norm = escalador.fit_transform(X_treino)
    X_teste_norm = escalador.transform(X_teste)

    # Lista de modelos para análise
    algoritmos = {
        'Regressão Linear': LinearRegression(),
        'Floresta Aleatória': RandomForestRegressor(n_estimators=100, random_state=42),
        'Árvores Extras': ExtraTreesRegressor(n_estimators=100, random_state=42),
        'Boosting Gradiente': GradientBoostingRegressor(n_estimators=100, random_state=42),
        'KNN': KNeighborsRegressor(n_neighbors=5),
        'SVR': SVR(kernel='rbf')
    }

    # Avaliação de cada modelo
    resultados = {}
    for nome, modelo in algoritmos.items():
        print(f"\nModelo: {nome}")

        # Validação cruzada
        scores_cv = cross_val_score(modelo, X_treino_norm, y_treino, cv=5, scoring='r2')

        # Treinamento e predição
        modelo.fit(X_treino_norm, y_treino)
        y_pred = modelo.predict(X_teste_norm)

        resultados[nome] = {
            'R2_CV': scores_cv.mean(),
            'Desvio_CV': scores_cv.std(),
            'R2_Teste': r2_score(y_teste, y_pred),
            'RMSE_Teste': np.sqrt(mean_squared_error(y_teste, y_pred)),
            'MAE_Teste': mean_absolute_error(y_teste, y_pred)
        }

        print(f"R² Médio CV: {resultados[nome]['R2_CV']:.4f}")
        print(f"R² Teste: {resultados[nome]['R2_Teste']:.4f}")

    return resultados, algoritmos, (X_treino_norm, X_teste_norm, y_treino, y_teste)

def main():
    # 1. Processamento inicial
    dados = carregar_dados()

    # 2. Investigação dos dados
    dados = explorar_dados(dados)

    # 3. Engenharia de variáveis
    X, y, atributos = preparar_variaveis(dados)

    # 4. Treinamento e avaliação
    resultados, modelos, (X_treino, X_teste, y_treino, y_teste) = treinar_modelos(X, y)

    # Exibindo o modelo de melhor desempenho
    melhor_modelo = max(resultados.items(), key=lambda x: x[1]['R2_Teste'])[0]
    print(f"\nModelo mais eficaz: {melhor_modelo}")

if __name__ == "__main__":
    main()
