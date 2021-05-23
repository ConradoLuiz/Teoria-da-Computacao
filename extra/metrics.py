from functools import wraps
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
    len_palavras = []
    timings = []

    for _ in range(1000):
        
        i = np.random.randint(0, 1000)
        j = np.random.randint(0, 1000)

        n1 = bin(i)
        n2 = bin(j)
        fita = [*n1[2:], '+', *n2[2:]]
        len_palavras.append(len(fita))
        result = bin(i + j)[2:]
        print(i, j)
        ts = time()
        fita_resultante, ponteiro = movimento(M, fita)
        te = time()

        timings.append((te-ts) * 1000)
        
        result_mt = ''.join(read_strip_until_end(fita_resultante, ponteiro))

    X = sm.add_constant(len_palavras)
    model = sm.OLS(timings, X)
    result = model.fit()

    regression_line = [result.params[0] + result.params[1]*len_palavra for len_palavra in len_palavras]

    exp, _ = curve_fit(lambda t, a, b: a*np.exp(b*t), len_palavras, timings)

    exp_x = np.linspace(min(len_palavras), max(len_palavras))
    exponential_line = [exp[0]*np.exp(exp[1]*x) for x in exp_x]
    
    fig, ax = plt.subplots()
    
    ax.plot(len_palavras, regression_line, c='m', label='Regressão Linear')
    ax.plot(exp_x, exponential_line, c='r', label='Regressão Exponencial')

    ax.scatter(len_palavras, timings)
    ax.legend()
    ax.set_title('Complexidade Temporal')
    ax.set_xlabel('|w|')
    ax.set_ylabel('Milissegundos')
    plt.show()   