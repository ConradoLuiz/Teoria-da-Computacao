from time import time
import matplotlib.pyplot as plt
import statsmodels.api as sm
from main import movimento, read_strip_until_end
from add import M
from scipy.optimize import curve_fit
import numpy as np

if __name__ == '__main__':
    np.random.seed(10)

    n_sucesso = 0
    metrics = {}

    for _ in range(1000):
        
        i = np.random.randint(0, 1000)
        j = np.random.randint(0, 1000)

        n1 = bin(i)
        n2 = bin(j)
        fita = [*n1[2:], '+', *n2[2:]]
        
        len_fita = len(fita)

        result = bin(i + j)[2:]
        print(i, j)
        
        fita_resultante, ponteiro, qtd_passos = movimento(M, fita)

        if len_fita not in metrics:
            metrics[len_fita] = qtd_passos

        elif qtd_passos > metrics[len_fita]:
            metrics[len_fita] = qtd_passos

        result_mt = ''.join(read_strip_until_end(fita_resultante, ponteiro))

    len_palavras = list(metrics.keys())
    timings = list(metrics.values())

    X = sm.add_constant(len_palavras)
    model = sm.OLS(timings, X)
    result = model.fit()

    regression_line = [result.params[0] + result.params[1]*len_palavra for len_palavra in len_palavras]
    
    fig, ax = plt.subplots()
    
    ax.plot(len_palavras, regression_line, c='m', label='Regressão Linear')

    ax.scatter(len_palavras, timings)
    ax.legend()
    ax.set_title('Complexidade Temporal de Pior Caso')
    ax.set_xlabel('|w|')
    ax.set_ylabel('Quatidade de passos')
    plt.show()   