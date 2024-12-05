import pandas as pd

url = "https://raw.githubusercontent.com/bluenex/WekaLearningDataset/master/bank/bank-data.csv"
arquivo = pd.read_csv(url)
arquivo.head()

print(arquivo.info())

print(arquivo.describe())

arquivo.pop('id')

arquivo.head()

print(arquivo['pep'].value_counts())

if 'sex' in arquivo.columns:
    print("Column 'sex' exists in the DataFrame.")

    arquivo['sex'] = arquivo['sex'].replace('MALE', 1)
    arquivo['sex'] = arquivo['sex'].replace('FEMALE', 0)
else:
    print("Column 'sex' does not exist in the DataFrame.")

print(arquivo.head())

if 'married' in arquivo.columns:
    print("Column 'pep' exists in the DataFrame.")
    arquivo['married'] = arquivo['married'].replace('YES', 1)
    arquivo['married'] = arquivo['married'].replace('NO', 0)
else:
    print("Column 'married' does not exist in the DataFrame.")

print(arquivo.head())

if 'car' in arquivo.columns:
    print("Column 'pep' exists in the DataFrame.")

    arquivo['car'] = arquivo['car'].replace('YES', 1)
    arquivo['car'] = arquivo['car'].replace('NO', 0)

else:
    print("Column 'car' does not exist in the DataFrame.")

print(arquivo.head())

if 'save_act' in arquivo.columns:
    print("Column 'save_act' exists in the DataFrame.")

    arquivo['save_act'] = arquivo['save_act'].replace('YES', 1)
    arquivo['save_act'] = arquivo['save_act'].replace('NO', 0)

else:
    print("Column 'save_act' does not exist in the DataFrame.")

print(arquivo.head())

if 'current_act' in arquivo.columns:
    print("Column 'current_act' exists in the DataFrame.")

    arquivo['current_act'] = arquivo['current_act'].replace('YES', 1)
    arquivo['current_act'] = arquivo['current_act'].replace('NO', 0)

else:
    print("Column 'current_act' does not exist in the DataFrame.")

print(arquivo.head())

if 'mortgage' in arquivo.columns:
    print("Column 'mortgage' exists in the DataFrame.")

    arquivo['mortgage'] = arquivo['mortgage'].replace('YES', 1)
    arquivo['mortgage'] = arquivo['mortgage'].replace('NO', 0)

else:
    print("Column 'mortgage' does not exist in the DataFrame.")

print(arquivo.head())

if 'pep' in arquivo.columns:
    print("Column 'pep' exists in the DataFrame.")

    arquivo['pep'] = arquivo['pep'].replace('YES', 1)
    arquivo['pep'] = arquivo['pep'].replace('NO', 0)
else:
    print("Column 'pep' does not exist in the DataFrame.")

print(arquivo.head())

arquivo = pd.get_dummies(arquivo, columns=['region'])

print(arquivo.head())

if 'sex_MALE' in arquivo.columns:
    print("Column 'sex_MALE' exists in the DataFrame.")

    arquivo['sex_MALE'] = arquivo['sex_MALE'].replace(True, 1)
    arquivo['sex_MALE'] = arquivo['sex_MALE'].replace(False, 0)
else:
    print("Column 'sex_MALE' does not exist in the DataFrame.")

print(arquivo.head())

if 'sex_FEMALE' in arquivo.columns:
    print("Column 'sex_FEMALE' exists in the DataFrame.")

    arquivo['sex_FEMALE'] = arquivo['sex_FEMALE'].replace(True, 1)
    arquivo['sex_FEMALE'] = arquivo['sex_FEMALE'].replace(False, 0)
else:
    print("Column 'sex_FEMALE' does not exist in the DataFrame.")

print(arquivo.head())

if 'region_INNER_CITY' in arquivo.columns:
    print("Column 'region_INNER_CITY' exists in the DataFrame.")

    arquivo['region_INNER_CITY'] = arquivo['region_INNER_CITY'].replace(True, 1)
    arquivo['region_INNER_CITY'] = arquivo['region_INNER_CITY'].replace(False, 0)
else:
    print("Column 'region_INNER_CITY' does not exist in the DataFrame.")

print(arquivo.head())

if 'region_RURAL' in arquivo.columns:
    print("Column 'region_RURAL' exists in the DataFrame.")

    arquivo['region_RURAL'] = arquivo['region_RURAL'].replace(True, 1)
    arquivo['region_RURAL'] = arquivo['region_RURAL'].replace(False, 0)
else:
    print("Column 'region_RURAL' does not exist in the DataFrame.")

print(arquivo.head())

if 'region_SUBURBAN' in arquivo.columns:
    print("Column 'region_SUBURBAN' exists in the DataFrame.")

    arquivo['region_SUBURBAN'] = arquivo['region_SUBURBAN'].replace(True, 1)
    arquivo['region_SUBURBAN'] = arquivo['region_SUBURBAN'].replace(False, 0)
else:
    print("Column 'region_SUBURBAN' does not exist in the DataFrame.")

print(arquivo.head())

if 'region_TOWN' in arquivo.columns:
    print("Column 'region_TOWN' exists in the DataFrame.")

    arquivo['region_TOWN'] = arquivo['region_TOWN'].replace(True, 1)
    arquivo['region_TOWN'] = arquivo['region_TOWN'].replace(False, 0)
else:
    print("Column 'region_TOWN' does not exist in the DataFrame.")

print(arquivo.head())

y = arquivo['pep']
X = arquivo.drop('pep', axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=35)

from sklearn.svm import SVC
# Inicializando o classificador SVM com um kernel. O padrão é 'rbf', mas pode ser alterado para 'linear', 'poly', etc.
modelo = SVC(kernel='rbf',probability=True)

modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

resultado = modelo.score(x_test, y_test)
print ("Acurácia:", resultado)

import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

y_pred = modelo.predict(x_test)
y_pred_rounded = np.round(y_pred)

precisao = precision_score(y_test, y_pred_rounded)
recall = recall_score(y_test, y_pred_rounded)
f1 = f1_score(y_test, y_pred_rounded)

print("Precisão:", precisao)
print("Recall:", recall)
print("F1-score:", f1)

from sklearn.metrics import confusion_matrix, classification_report

"""
Calculando e exibindo a matriz de confusão. A orientação padrão é a seguinte:
[0,0]: Verdadeiros Negativos (VN) - Previsões corretamente identificadas como negativas.
[0,1]: Falsos Positivos (FP) - Previsões incorretamente identificadas como positivas.
[1,0]: Falsos Negativos (FN) - Previsões incorretamente identificadas como negativas.
[1,1]: Verdadeiros Positivos (VP) - Previsões corretamente identificadas como positivas.
"""

conf_matrix = confusion_matrix(y_test, y_pred_rounded)
print("Matriz de Confusão:")
print(conf_matrix)

"""
Calculando e exibindo as métricas de classificação.
Se algumas classes têm muito mais amostras do que outras, isso pode influenciar o desempenho e confiabilidade do modelo.

O "support" refere-se à quantidade de ocorrências da classe específica no conjunto de dados, sendo útil para verificar desbalanceamentos.
A "macro avg" calcula a média aritmética das métricas (precisão, recall, F1-score) para cada classe, sem considerar o número de instâncias em cada classe (support).
A "weighted avg" calcula a média ponderada das métricas para cada classe, considerando o número de instâncias em cada classe (support).
"""
print("Relatório de Classsificação:")
print(classification_report(y_test, y_pred_rounded))