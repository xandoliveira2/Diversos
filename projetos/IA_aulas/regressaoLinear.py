from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error ,mean_absolute_error #mean_squared_log_error _> caso precise
from sklearn.model_selection import train_test_split
from math import sqrt
# criando tabela de dados
df = pd.read_csv("regressaoLinearDados.csv")

# pegando os dados de motor e co2
motores = pd.DataFrame(df['ENGINESIZE'])
co2 = df[['CO2EMISSIONS']]

# separando a parte que será para treino da 'IA' e a parte que sera de teste para verificar a 'eficiencia'
motores_treino,motores_teste,co2_treino,co2_teste = train_test_split(motores,co2,test_size=0.2,random_state=42)

# exibir o gráfico
# plt.scatter(motores_treino,co2_treino,color="green")
# plt.xlabel("Motores")
# plt.ylabel("Emissão de CO2")
# plt.show()


# criando modelo para regressão linear
modelo = linear_model.LinearRegression()
#treinando o modelo com dados para encontrar valor de A e B ( Y = A + B * X )
modelo.fit(motores_treino,co2_treino)
# exibindo A - intercepto e B - inclinação:
print(modelo.intercept_)
print(modelo.coef_)

# # exibindo a linha no gráfico
# plt.scatter(motores_treino,co2_treino, color="green")
# # cria a linha onde:
# plt.plot(motores_treino,modelo.coef_[0][0]*motores_treino + modelo.intercept_[0],'-b')
# # primeiro parametro é qual campo ele vai interligar
# # o segundo é com quem ele vai ligar, então o primeiro ponto no gráfico será criado com base na sua linha 'média'
# # terceiro = a cor da linha e o tipo,  - significa linha continua e b a cor ( b-blue )
# plt.xlabel("Motores")
# plt.ylabel("Emissão de CO2")
# # plt.show()

# prever valores de dados de motores no modelo treinado
predicoes = modelo.predict(motores_teste)

plt.scatter(motores_teste,co2_teste, color="green")
plt.plot(motores_teste,modelo.coef_[0][0]*motores_teste + modelo.intercept_[0],'-b')
plt.xlabel("Motores")
plt.ylabel("Emissão de CO2")
# plt.show()


# mostrar métricas:
print(f"Soma dos erros ao quadrado (SSE): {round(float(np.sum((predicoes-co2_teste)**2)))}")
print(f"Erro quadrático médio (MSE): {mean_squared_error(co2_teste,predicoes):.2f}")
print(f"Erro médio absoluto (MAE): {mean_absolute_error(co2_teste,predicoes):.2f}")
print(f"Raiz do erro quadrático médio (RMSE): {sqrt(mean_squared_error(co2_teste,predicoes)):.2f}")
print(f"R2 score: {r2_score(predicoes,co2_teste):.2f}")
