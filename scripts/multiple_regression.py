"""Funções para Análise de Regressão Linear Múltipla"""


import numpy as np


def y_mean(y_vet):
    """Função que calcula a media da variável y da amostra"""
    return sum(list(y_vet))/len(list(y_vet))

def X_multi(matrix):
    """Calcula a matriz multivariada dos x_i"""
    np_matrix = np.array(matrix)
    ones_column = np.array([np.ones(len(matrix))]).T
    new_matrix = np.hstack((ones_column, matrix))
    X = np.delete(new_matrix, np.size(new_matrix, 1) - 1, 1)
    return X

def X_polinomial(x_vet, grade):
    """
    Define a matriz dos x com numero de colunas dado pelo argumento
    columns. O número de colunas da matriz X representa o grau da
    função polinomial em questão. 
    """
    vet = np.array(
        [
            [x**n for n in range(grade + 1)] \
                for x in x_vet
        ]
    )
    return vet

def Y(y_vet):
    """Define o vetor das variáveis de resultados y."""
    return np.array([y_vet]).T

def beta(X, Y):
    """beta =(X^T*X)^(−1)*X^T*Y"""
    inv_Xt_X = np.linalg.inv(np.dot(X.T,X))
    B = np.dot(np.dot(inv_Xt_X, X.T),Y)
    return B


def Y_estimator_polinomial(x_vet, y_vet, grade):
    """Calcula os pontos da curva estimada de regressão, para o polinomio de grau <grade>"""
    matrix_X = X_polinomial(x_vet,grade)
    matrix_Y = Y(y_vet)
    return np.dot(matrix_X, beta(matrix_X, matrix_Y))

def Y_estimator_multi(matrix):
    np_matrix = np.array(matrix)
    X = X_multi(matrix)
    Y = np.array([np_matrix[:,np.size(np_matrix, 1) - 1]]).T
    y_estimated = np.dot(X, beta(X, Y))
    return y_estimated


def determinition_coefficient(y_vet, y_estimated):
    """Retorna o coeficiente de determinação de y"""
    # breakpoint()
    R_2 = 1 - sum((y_vet - y_estimated.T[0])**2)/sum((y_vet - y_mean(y_vet))**2)
    return R_2

def adjusted_determinition_coefficient(columns, y_vet, y_estimated):
    """Obtem o coeficiente de determinação ajustado para a regressão multipla."""
    
    p = columns + 1
    n = len(y_vet)
    Radj_2 = 1 - (sum((y_vet - y_estimated.T[0])**2)*(n-1))/((n-p)*sum((y_vet - y_mean(y_vet))**2))
    # breakpoint()
    return Radj_2