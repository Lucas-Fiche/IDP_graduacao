import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import randint
from sklearn.ensemble import IsolationForest, ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Carregando o Dataset
url = 'https://raw.githubusercontent.com/klaytoncastro/idp-machinelearning/main/california/california_housing.csv'
df = pd.read_csv(url, delimiter = ',', decimal = '.')
df.head()

# Verificando a estrutura de dados
df.info()

# Calculando as correlações entre as variáveis ​​preditoras e a variável alvo
correlations = df.corr()['MedHouseVal'].sort_values(ascending=False)
print(correlations)

# Verificando a distribuição dos dados
df.describe()

# Professor - Distância para San Francisco
df['DistanceFromSF'] = np.sqrt((df['Latitude'] - 37.7749)**2 + (df['Longitude'] + 122.4194)**2)

df.head()

# retirar os outliers
# plotar o gráfico do cotovelo
# Usar o kmean em função da latitude e longitude (criando a coluna Geocluster para armazenar os resultados)
# Ver a matriz de correlação

#Contagem de números entre 0 e 1

print("Contagem de valores entre 0 e 1 em cada coluna:")
for column in df.columns:
    count_decimais = ((df[column] > 0) & (df[column] < 1)).sum()
    print(f"{column}: {count_decimais}")

for col in ['AveRooms', 'AveBedrms']:
  df.loc[(df[col] > 0) & (df[col] < 1), col] = 1

#FEITO
#Contagem de números entre 0 e 1

print("Contagem de valores iguais a 5 em MedHouseVal:")
for column in df.columns:
    count_cinco = ((df[column] >= 5)).sum()
    print(f"{column}: {count_cinco}")

df['MedHouseVal'][df['MedHouseVal'] >= 5] = np.nan

df = df.dropna()
df.describe()

df.head()

# FEITO
# Indentificando os valores negativos na tabela

print("Contagem de valores Negativos em cada coluna:")
for column in df.columns:
    count_negative = (df[column] < 0).sum()
    print(f"{column}: {count_negative}")

df.head()

# Hipótese 2: Como ainda teremos em torno de 7000 observações na amostra após remover os dados ausentes, decidimos removê-los para assegurar maior fidelidade.
df = df.dropna()
df.describe()

# As distribuições parecem melhores agora. Vamos exibir a nova matriz de correlação para análise.

correlation_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin = -1)
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.show()

df.head()

# Calculando as correlações entre as variáveis ​​preditoras e a variável alvo
correlations = df.corr()['MedHouseVal'].sort_values(ascending=False)
print(correlations)

# Preparando as variáveis para treinar o modelo.
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar com o ExtraTrees
#model = ExtraTreesRegressor(random_state=7, n_estimators=67, max_features='sqrt', max_depth=100, min_samples_split=13, min_samples_leaf=1, bootstrap = False)
#model = ExtraTreesRegressor(random_state=42, n_estimators=350, max_features='sqrt', max_depth=None, min_samples_split=2, min_samples_leaf=1)
model = ExtraTreesRegressor();
model.fit(X_train, y_train)

# Fazer testes com RandomForest
# Fazer testes com LightGBM
# Fazer testes com XGBoost

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Fazer previsões
y_pred = model.predict(X_test)

# Calcular métricas
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R² Score: {r2}')

# Gráfico de valores previstos x valores atuais
plt.figure(figsize=(10, 6))
plt.scatter(x=y_test, y=y_pred, color='blue', label='Valores Previstos')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Ideal Line')
plt.xlabel('Valores reais')
plt.ylabel('Valores Previstos')
plt.title('Valores previstos x Valores reais')
plt.legend()
plt.show()
# O gráfico terá dados lineares no valor 5 por limitação do DataSet, uma vez que todas as casas que ultrapassam o valor de 500.000 são arredondadas para 5.

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Passo 1: Definir o espaço de busca dos hiperparâmetros
param_grid = {
    'n_estimators': [100, 200, 300],     # Número de árvores na floresta
    'max_depth': [None, 10, 20, 30],     # Profundidade máxima das árvores
    'min_samples_split': [2, 5, 10],     # Número mínimo de amostras para dividir um nó
    'min_samples_leaf': [1, 2, 4]        # Número mínimo de amostras em um nó folha
}

# Passo 2: Configurar o GridSearchCV
grid_search = GridSearchCV(
    estimator=ExtraTreesRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,                      # Número de folds para validação cruzada
    scoring='neg_mean_squared_error',  # Métrica de avaliação
    verbose=1,                 # Nível de verbosidade
    n_jobs=-1                  # Usar todos os processadores disponíveis
)

# Passo 3: Treinar o GridSearchCV
grid_search.fit(X_train, y_train)

# Passo 4: Avaliar o melhor modelo
best_model = grid_search.best_estimator_
print("Melhores hiperparâmetros encontrados:", grid_search.best_params_)

# Fazer previsões e calcular métricas
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R² Score: {r2}')

from sklearn.model_selection import RandomizedSearchCV

# Passo 1: Definir o espaço de busca dos hiperparâmetros
param_dist = {
    'n_estimators': [50, 100, 200, 300, 500],
    'max_depth': [None, 10, 20, 30, 50],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]  # Usar ou não amostragem com reposição
}

# Passo 2: Configurar o RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=ExtraTreesRegressor(random_state=42),
    param_distributions=param_dist,
    n_iter=100,  # Número de combinações de hiperparâmetros para amostrar
    cv=5,
    scoring='neg_mean_squared_error',
    verbose=1,
    random_state=42,
    n_jobs=-1
)

# Passo 3: Treinar o RandomizedSearchCV
random_search.fit(X_train, y_train)

# Passo 4: Avaliar o melhor modelo
best_model = random_search.best_estimator_
print("Melhores hiperparâmetros encontrados:", random_search.best_params_)

# Fazer previsões e calcular métricas
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R² Score: {r2}')